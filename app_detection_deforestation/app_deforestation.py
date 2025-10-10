import io
import math
import json
from pathlib import Path
import base64

import numpy as np
import requests
import streamlit as st
from PIL import Image, ImageDraw
import mercantile
import folium
from folium.plugins import Draw
from streamlit_folium import st_folium

# ==========================================================
#  Setup & CSS
# ==========================================================
try:
    from streamlit_javascript import st_javascript
except Exception:
    def st_javascript(*args, **kwargs):
        return None



def set_bg_color(color="#0D1B2A", text="#F5F6FA",
                 secondary="#1B263B", sidebar_text="#F5F6FA"):
    st.markdown(f"""
    <style>
    /* page */
    [data-testid="stAppViewContainer"] {{
        background: {color} !important;
    }}
    /* sidebar */
    [data-testid="stSidebar"] > div:first-child {{
        background: {secondary} !important;
        color: {sidebar_text} !important;
    }}
    [data-testid="stSidebar"] * {{ color: {sidebar_text} !important; }}
    /* texte global */
    .stApp, .stApp * {{ color: {text}; }}
    </style>
    """, unsafe_allow_html=True)


def set_bg_image_url(url: str, cover=True, fixed=True):
    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{url}");
        background-repeat: no-repeat;
        background-position: center center;
        {"background-size: cover;" if cover else ""}
        {"background-attachment: fixed;" if fixed else ""}
    }}
    </style>
    """, unsafe_allow_html=True)


def set_bg_image_local(path: str, cover=True, fixed=True):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{data}");
        background-repeat: no-repeat;
        background-position: center center;
        {"background-size: cover;" if cover else ""}
        {"background-attachment: fixed;" if fixed else ""}
    }}
    </style>
    """, unsafe_allow_html=True)


st.set_page_config(
    page_title="Détection de la déforestation en Amazonie – sélection de zone et inférence",
    page_icon="🌳",  # 👈 ajoute l’emoji ici !
    layout="wide"
)
set_bg_color(color="#0D1B2A", text="#F5F6FA", secondary="#1B263B", sidebar_text="#F5F6FA")





st.markdown(
    """
    <style>
    /* Sidebar tip */
    [data-testid="stSidebar"] .tip {
        color: #ffffff !important; opacity: 1 !important;
        font-size: 0.95rem; line-height: 1.5;
    }
    [data-testid="stSidebar"] .tip strong { color: #ffffff !important; }

    /* Supprimer l'espace sous st_folium */
    div[data-testid="stComponent"] { margin-bottom: 0 !important; }

    /* Boutons verts personnalisés */
    div.stButton > button:first-child {
        background-color: #28a745 !important; color: white !important;
        border: none !important; border-radius: 6px !important;
        font-weight: 600 !important; transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: #218838 !important; transform: scale(1.03);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# JS : tuer le spacer autour de l'iframe au premier rendu
st_javascript("""
(() => {
  const fix = () => {
    const iframes = parent.document.querySelectorAll('iframe[title="st_folium"]');
    if (!iframes.length) return;
    const ifr = iframes[iframes.length - 1];
    const wrap = ifr.closest('div[data-testid="stComponent"]');
    if (wrap) {
      wrap.style.marginBottom = '0px';
      const sib = wrap.nextElementSibling;
      if (sib && sib.style && sib.style.height) sib.style.height = '0px';
    }
  };
  fix();
  const obs = new MutationObserver(() => fix());
  obs.observe(parent.document.body, { childList: true, subtree: true });
  setTimeout(fix, 120);
})();
""")

st.title("🛰️ Détection de la déforestation en Amazonie – sélection de zones et inférence")

# ==========================================================
#  Constantes / helpers carte
# ==========================================================
ESRI_URL    = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
TILE_SIZE   = 256
USER_AGENT  = "Mozilla/5.0 (BBox Exporter - Streamlit)"
EXPORT_ZOOM = 11
MAP_HEIGHT  = 600

def clamp_lat(lat: float) -> float:
    MAX_LAT = 85.05112878
    return max(min(lat, MAX_LAT), -MAX_LAT)

def lonlat_to_global_pixels(lon: float, lat: float, z: int):
    lat = clamp_lat(lat)
    siny = math.sin(math.radians(lat))
    n = 2.0 ** z
    x = (lon + 180.0) / 360.0 * n * TILE_SIZE
    y = (0.5 - math.log((1 + siny) / (1 - siny)) / (4 * math.pi)) * n * TILE_SIZE
    return x, y

def fetch_tile(z: int, x: int, y: int, timeout: int = 15) -> Image.Image:
    url = ESRI_URL.format(z=z, x=x, y=y)
    resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
    resp.raise_for_status()
    from PIL import Image as PILImage  # éviter confusion import
    return PILImage.open(io.BytesIO(resp.content)).convert("RGB")

def stitch_tiles_to_bytes(bbox, z: int, add_attribution: bool = True) -> bytes:
    min_lon, min_lat, max_lon, max_lat = bbox
    min_px, max_py = lonlat_to_global_pixels(min_lon, min_lat, z)
    max_px, min_py = lonlat_to_global_pixels(max_lon, max_lat, z)

    tiles = list(mercantile.tiles(min_lon, min_lat, max_lon, max_lat, [z]))
    if not tiles:
        raise ValueError("Aucune tuile à ce zoom; ajuste le niveau de zoom ou le rectangle.")
    xs = [t.x for t in tiles]; ys = [t.y for t in tiles]
    x_min, x_max = min(xs), max(xs); y_min, y_max = min(ys), max(ys)

    W = (x_max - x_min + 1) * TILE_SIZE
    H = (y_max - y_min + 1) * TILE_SIZE
    from PIL import Image as PILImage
    mosaic = PILImage.new("RGB", (W, H))

    for ty in range(y_min, y_max + 1):
        for tx in range(x_min, x_max + 1):
            try:
                im = fetch_tile(z, tx, ty)
            except Exception:
                im = PILImage.new("RGB", (TILE_SIZE, TILE_SIZE), (0, 0, 0))
            mosaic.paste(im, ((tx - x_min) * TILE_SIZE, (ty - y_min) * TILE_SIZE))

    canvas_min_px = x_min * TILE_SIZE
    canvas_min_py = y_min * TILE_SIZE
    L = int(round(min_px - canvas_min_px))
    T = int(round(min_py - canvas_min_py))
    R = int(round(max_px - canvas_min_px))
    B = int(round(max_py - canvas_min_py))

    L = max(0, min(L, mosaic.width));  R = max(0, min(R, mosaic.width))
    T = max(0, min(T, mosaic.height)); B = max(0, min(B, mosaic.height))
    if R <= L or B <= T:
        raise ValueError("Découpe invalide; réessaie avec un autre zoom ou rectangle.")

    out_img = mosaic.crop((L, T, R, B))

    if add_attribution:
        from PIL import Image as PILImage
        pad = 18
        with_pad = PILImage.new("RGB", (out_img.width, out_img.height + pad), (255, 255, 255))
        with_pad.paste(out_img, (0, 0))
        ImageDraw.Draw(with_pad).text(
            (6, out_img.height + 2),
            "Imagery © Esri, Maxar, Earthstar Geographics, and the GIS User Community",
            fill=(0, 0, 0),
        )
        out_img = with_pad

    buf = io.BytesIO()
    out_img.save(buf, format="PNG")
    buf.seek(0)
    return buf.getvalue()

def extract_bbox_from_stfolium(return_dict):
    gj = return_dict.get("last_active_drawing")
    if not gj:
        gj = return_dict.get("last_drawn_geojson")
    if not gj:
        drawings = return_dict.get("all_drawings")
        if drawings:
            gj = drawings[-1]
    if not gj:
        return None
    try:
        if gj.get("geometry", {}).get("type") == "Polygon":
            coords = gj["geometry"]["coordinates"][0]
            lons = [c[0] for c in coords]; lats = [c[1] for c in coords]
            return (min(lons), min(lats), max(lons), max(lats))
    except Exception:
        pass
    return None

# --------------- Helpers GeoJSON ---------------
def _iter_coords(geom):
    gtype = geom.get("type"); coords = geom.get("coordinates")
    if gtype == "Point":
        yield coords
    elif gtype in ("MultiPoint", "LineString"):
        for c in coords: yield c
    elif gtype in ("MultiLineString", "Polygon"):
        for part in coords:
            for c in part: yield c
    elif gtype == "MultiPolygon":
        for poly in coords:
            for ring in poly:
                for c in ring: yield c
    elif gtype == "GeometryCollection":
        for g in geom.get("geometries", []):
            yield from _iter_coords(g)

def geojson_bounds(gj: dict):
    def update_from_geom(geom, acc):
        for lon, lat in _iter_coords(geom):
            acc["min_lon"] = min(acc["min_lon"], lon)
            acc["max_lon"] = max(acc["max_lon"], lon)
            acc["min_lat"] = min(acc["min_lat"], lat)
            acc["max_lat"] = max(acc["max_lat"], lat)

    acc = dict(min_lon=+1e9, max_lon=-1e9, min_lat=+1e9, max_lat=-1e9)
    try:
        if gj.get("type") == "FeatureCollection":
            for feat in gj.get("features", []):
                geom = feat.get("geometry")
                if geom: update_from_geom(geom, acc)
        elif gj.get("type") == "Feature":
            geom = gj.get("geometry")
            if geom: update_from_geom(geom, acc)
        else:
            update_from_geom(gj, acc)
    except Exception:
        return None, None

    if acc["min_lon"] > acc["max_lon"] or acc["min_lat"] > acc["max_lat"]:
        return None, None

    bounds = [[acc["min_lat"], acc["min_lon"]], [acc["max_lat"], acc["max_lon"]]]
    center = ((acc["min_lat"] + acc["max_lat"]) / 2.0, (acc["min_lon"] + acc["max_lon"]) / 2.0)
    return bounds, center

# État de centrage par défaut (session)
if "map_center" not in st.session_state:
    st.session_state["map_center"] = (-3.1, -60.0)  # (lat, lon)
if "map_zoom" not in st.session_state:
    st.session_state["map_zoom"] = 5

if "map_nonce" not in st.session_state:
    st.session_state["map_nonce"] = 0

# ==========================
#  Sidebar (GeoJSON d'abord)
# ==========================
with st.sidebar:
    # --- 1) GeoJSON en premier ---
    st.subheader("Centrage de la carte grâce à un GeoJSON importer en local")
    geojson_file = st.file_uploader(
        "Charger un GeoJSON (WGS84)",
        type=["geojson", "json"],
        key="gj_upload"
    )
    center_on_gj = st.button("📍 Centrer la carte sur le GeoJSON", key="btn_center_gj")

    gj_data = None
    if geojson_file is not None:
        try:
            gj_bytes = geojson_file.getvalue() if hasattr(geojson_file, "getvalue") else (
                geojson_file.read() or (geojson_file.seek(0) or geojson_file.read())
            )
            gj_text = gj_bytes.decode("utf-8")
            gj_data = json.loads(gj_text)

            if center_on_gj:
                bounds, center = geojson_bounds(gj_data)
                if bounds:
                    st.session_state["map_center"] = center
                    st.session_state["map_zoom"] = 8
                    # si tu as ajouté le nonce pour reconstruire l'iframe :
                    if "map_nonce" in st.session_state:
                        st.session_state["map_nonce"] += 1
                    st.success("Carte centrée sur le GeoJSON.")
                else:
                    st.warning("Impossible de calculer les bornes du GeoJSON (coordonnées manquantes ?).")
        except Exception as e:
            st.error(f"GeoJSON invalide : {e}")

    st.markdown("---")

    # --- 2) Conseils ensuite ---
    st.header("Comment booster la détection ? ")
    st.markdown(
        """ <div class="tip"> 💡 <strong>Conseil :</strong><br>
        Choisir un niveau d'
        <strong>échelle cartographique d’environ 1 :150 000</strong>,
        soit une <strong>barre d’échelle d’environ 10 km</strong> visible sur la carte.<br>
        Et dessiner un rectangle de <strong>1/10 la taille de la carte</strong> 
        Ce niveau offre un bon compromis entre zone couverte et détails visibles,
        et améliore la qualité des prédictions de déforestation. </div> """,
        unsafe_allow_html=True,
    )

# attribution forcée activée par défaut (plus de case à cocher)
add_attr = True

# ==========================================================
#  Carte Folium (centrée via session) + Draw
# ==========================================================
CENTER_LAT, CENTER_LON = st.session_state["map_center"]

m = folium.Map(
    location=[CENTER_LAT, CENTER_LON],
    zoom_start=st.session_state["map_zoom"],
    tiles=None,
    control_scale=True,
    height=MAP_HEIGHT,
)

# Forcer hauteur dès le premier paint
_map_id = m.get_name()
m.get_root().header.add_child(folium.Element(f"""
<style>
html, body {{ height: {MAP_HEIGHT}px !important; margin: 0; padding: 0; }}
.folium-map, .leaflet-container {{ height: {MAP_HEIGHT}px !important; }}
#{_map_id} {{ height: {MAP_HEIGHT}px !important; width: 100% !important; }}
</style>
"""))

folium.TileLayer(
    tiles=ESRI_URL,
    attr="Esri, Maxar, Earthstar Geographics, and the GIS User Community",
    name="Esri World Imagery",
    overlay=False,
    control=True,
).add_to(m)

Draw(
    export=False,
    draw_options={
        "polyline": False, "polygon": False, "circle": False, "circlemarker": False,
        "marker": False, "rectangle": True
    },
    edit_options={"edit": True, "remove": True},
).add_to(m)

# Afficher GeoJSON (overlay) si chargé
if geojson_file is not None and gj_data is not None:
    try:
        folium.GeoJson(
            gj_data,
            name="Zone GeoJSON",
            style_function=lambda f: {"color": "#ff7800", "weight": 2, "fillOpacity": 0.05},
            highlight_function=lambda f: {"weight": 3, "color": "#ff5500"},
        ).add_to(m)
    except Exception:
        pass

st.markdown("""
- Naviguer sur la carte ou centrer la carte grâce à l'import d'un Geojson           
- Zoomez jusqu’à une **échelle ≈ 1:150 000** (barre d’échelle **10 km**) pour de meilleures performances de détection. 
- Dessinez un rectangle avec l'outil ⬛, puis cliquez **Exporter PNG** (bouton en bas de la page ou rafraîchir la page pour l'approcher)
""")

ret = st_folium(
    m,
    height=MAP_HEIGHT,
    use_container_width=True,
    returned_objects=["last_active_drawing", "all_drawn_geojson", "all_drawings"],
    key=f"map_main_{st.session_state['map_nonce']}",    # <-- here
)


# ==========================================================
#  Export PNG
# ==========================================================
col1, col2 = st.columns([1, 3])
with col1:
    do_export = st.button("📸 Exporter PNG")
with col2:
    bbox = extract_bbox_from_stfolium(ret) if ret else None
    st.write("**BBox courant :**", bbox if bbox else "— (aucun rectangle détecté)")

if do_export:
    if not bbox:
        st.warning("Trace d’abord un rectangle sur la carte.")
    else:
        try:
            png_bytes = stitch_tiles_to_bytes(bbox, z=EXPORT_ZOOM, add_attribution=add_attr)
            st.success("PNG généré en mémoire ✅")
            st.image(png_bytes, caption=f"Export bbox @ zoom {EXPORT_ZOOM}", use_column_width=True)
            st.download_button("💾 Télécharger le PNG", data=png_bytes, file_name="export_bbox.png", mime="image/png")
            st.session_state["last_export_png"] = png_bytes
        except Exception as e:
            st.error(f"Erreur pendant l’export: {e}")

# ==========================================================
#  Inférence TFLite (robuste 4/5 champs + bump cache)
# ==========================================================
st.markdown("---")
show_infer = st.session_state.get("show_infer", False)
if st.button("🧠 Tester l'inférence (Resnet finetuned)"):
    show_infer = True
    st.session_state["show_infer"] = True

if show_infer:
    import tensorflow as tf
    from tensorflow.keras.applications.resnet import preprocess_input
    from PIL import Image as PILImage

    BASE_DIR   = Path(__file__).parent
    EXPORT_DIR = BASE_DIR / "export"
    MODEL_PATH = EXPORT_DIR / "final_resnet_tf215_int8.tflite"
    CONFIG_PATH = BASE_DIR / "export" / "model_config.json"

    CLASS_NAMES = ["no_deforestation", "deforestation"]
    IMG_SIZE = (224, 224)
    THRESHOLD = 0.5

    if CONFIG_PATH.exists():
        try:
            cfg = json.loads(CONFIG_PATH.read_text())
            CLASS_NAMES = cfg.get("class_names", CLASS_NAMES)
            IMG_SIZE = tuple(cfg.get("img_size", list(IMG_SIZE)))
        except Exception as e:
            st.warning(f"Impossible de lire {CONFIG_PATH.name} : {e}")

    def _get(d, key, default=None):
        if isinstance(d, dict): return d.get(key, default)
        return getattr(d, key, default)

    def _get_quant_params(d):
        q = _get(d, "quantization", None)
        if isinstance(q, tuple) and len(q) == 2:
            return float(q[0]), int(q[1])
        qp = _get(d, "quantization_parameters", None)
        if qp is not None:
            scales = getattr(qp, "scales", None)
            zps    = getattr(qp, "zero_points", None)
            if scales is not None and len(scales) > 0:
                zp0 = int(zps[0]) if (zps is not None and len(zps) > 0) else 0
                return float(scales[0]), zp0
            if isinstance(qp, dict) and "scales" in qp:
                sc = qp["scales"]; zp = qp.get("zero_points", [0])
                if len(sc) > 0:
                    return float(sc[0]), int(zp[0] if len(zp) > 0 else 0)
        return 0.0, 0

    def _tensor_index(d):
        for k in ("index", "tensor_index"):
            v = _get(d, k, None)
            if v is not None:
                return int(v)
        raise ValueError(f"Impossible de trouver l'index du tenseur dans: {d}")

    # --- helper robuste (4 ou 5 champs)
    def _unpack_io(meta_io, label="io"):
        if len(meta_io) == 5:
            idx, dtype, shape, scale, zp = meta_io
        elif len(meta_io) == 4:
            idx, dtype, shape, scale = meta_io
            zp = 0
        else:
            raise ValueError(f"meta['{label}'] inattendu (len={len(meta_io)}): {meta_io}")
        return idx, dtype, shape, scale, zp

    @st.cache_resource(show_spinner="Chargement du modèle TFLite...")
    def load_tflite(path: Path, cache_version: int = 2):
        if not path.exists():
            raise FileNotFoundError(f"Modèle introuvable : {path}")
        intr = tf.lite.Interpreter(model_path=str(path))
        intr.allocate_tensors()
        in_det  = intr.get_input_details()[0]
        out_det = intr.get_output_details()[0]
        in_dtype  = _get(in_det, "dtype");  out_dtype = _get(out_det, "dtype")
        in_shape  = _get(in_det, "shape");  out_shape = _get(out_det, "shape")
        in_scale,  in_zp  = _get_quant_params(in_det)
        out_scale, out_zp = _get_quant_params(out_det)
        in_index  = _tensor_index(in_det)
        out_index = _tensor_index(out_det)
        return {
            "interpreter": intr,
            "in":  (in_index,  in_dtype,  in_shape,  in_scale,  in_zp),
            "out": (out_index, out_dtype, out_shape, out_scale, out_zp),
            "name": path.name,
            "cache_version": cache_version,
        }

    def _tflite_quantize(x_fp32, in_dtype, scale, zp):
        if in_dtype == np.int8 and scale > 0:
            x_q = np.round(x_fp32 / scale + zp)
            return np.clip(x_q, -128, 127).astype(np.int8)
        return x_fp32.astype(in_dtype)

    def _tflite_dequantize(y, out_dtype, scale, zp):
        if out_dtype == np.int8 and scale > 0:
            return (y.astype(np.float32) - zp) * scale
        return y.astype(np.float32)

    def preprocess_pil(img: PILImage.Image, img_size=IMG_SIZE):
        x = np.asarray(img.convert("RGB").resize(img_size), dtype=np.float32)
        from tensorflow.keras.applications.resnet import preprocess_input as _pp
        x = _pp(x)
        return np.expand_dims(x, 0)

    def predict_tflite_tta(meta, x):
        intr = meta["interpreter"]
        in_index,  in_dtype,  _, in_scale,  in_zp  = _unpack_io(meta["in"],  "in")
        out_index, out_dtype, _, out_scale, out_zp = _unpack_io(meta["out"], "out")

        def run_once(v):
            x_in = _tflite_quantize(v, in_dtype, in_scale, in_zp)
            intr.set_tensor(in_index, x_in)
            intr.invoke()
            y = intr.get_tensor(out_index)
            return _tflite_dequantize(y, out_dtype, out_scale, out_zp)

        def np_flip_lr(a): return a[:, :, ::-1, :]
        def np_flip_ud(a): return a[:, ::-1, :, :]
        def np_rot90(a,k=1): return np.rot90(a, k=k, axes=(1,2)).copy()

        views = [x, np_flip_lr(x), np_flip_ud(x), np_rot90(x,1), np_rot90(x,2), np_rot90(x,3)]
        preds = [run_once(v) for v in views]
        return np.mean(np.stack(preds, axis=0), axis=0)

    # Chargement modèle (bump cache)
    tflite_meta = load_tflite(MODEL_PATH, cache_version=2)

    st.subheader("Tester une image")
    c_up, c_or, c_mem = st.columns([3, 1, 2])
    with c_up:
        uploaded = st.file_uploader("Choisissez une image (JPG/PNG)", type=["jpg","jpeg","png"], key="infer_uploader")
    with c_or:
        st.write(" ")
    with c_mem:
        use_saved = False
        if "last_export_png" in st.session_state:
            use_saved = st.button("Utiliser le dernier PNG exporté")

    infer_image = None
    if uploaded is not None:
        try:
            infer_image = PILImage.open(uploaded).convert("RGB")
        except Exception as e:
            st.error(f"Erreur d'ouverture de l'image : {e}")
            infer_image = None
    elif use_saved:
        try:
            infer_image = PILImage.open(io.BytesIO(st.session_state["last_export_png"])).convert("RGB")
        except Exception as e:
            st.error(f"Impossible d’ouvrir l’image exportée : {e}")
            infer_image = None

    if infer_image is None:
        st.info("📸 Importez une image, ou cliquez **Utiliser le dernier PNG exporté**.")
    else:
        st.image(infer_image, caption="Image pour l'inférence", use_column_width=False, width=infer_image.width, channels="RGB", output_format="PNG")

        with st.spinner("🧠 Inférence en cours..."):
            x = preprocess_pil(infer_image)
            proba = predict_tflite_tta(tflite_meta, x)[0]

        if len(CLASS_NAMES) == 2 and CLASS_NAMES[1] == "deforestation":
            p_def = float(proba[1]); is_def = p_def >= THRESHOLD
            decision = "🔥 **Déforestation détectée** 🚨" if is_def else "🌳 **Aucune déforestation** ✅"
            st.markdown(f"### {decision}")
            st.write(f"**Probabilité de déforestation :** `{p_def:.3f}` (seuil fixé à {THRESHOLD:.2f})")
        else:
            idx = int(np.argmax(proba))
            st.markdown(f"### Classe prédite : `{CLASS_NAMES[idx]}` ({proba[idx]:.3f})")

        st.write("**Détail des probabilités**")
        st.json({c: float(p) for c, p in zip(CLASS_NAMES, proba)})
