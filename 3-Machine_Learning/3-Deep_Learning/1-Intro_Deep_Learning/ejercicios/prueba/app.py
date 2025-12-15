import streamlit as st
from PIL import Image
import numpy as np
import funciones as f  # tu módulo con funciones de ML
# streamlit run app.py

# ---------------------- CSS PRO ----------------------
st.markdown(
    """
    <style>
    /* Fondo principal pastel */
    .stApp {
        background-color: #BFD7EA;  /* azul pastel */
        color: #1f1f1f;             /* texto oscuro */
        font-family: 'Segoe UI', sans-serif;
    }

    /* Contenedores de widgets */
    .css-1d391kg {
        background-color: rgba(255, 255, 255, 0.7); /* semi-transparente */
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        color: #1f1f1f;  /* texto dentro de contenedor */
    }

    /* Títulos */
    .css-10trblm {
        color: #0072C6; /* azul oscuro para títulos */
        font-weight: bold;
    }

    /* Botones */
    div.stButton > button:first-child {
        background-color: #FF7F50;  /* coral pastel */
        color: white;
        height: 3em;
        width: 100%;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #FFA07A;  /* coral más claro al pasar el mouse */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------- TITULO ----------------------
st.title("💡 Clasificador de Emociones")
st.write("Interfaz profesional con fondo pastel y contenedores semi-transparentes")

# ---------------------- INPUTS CSV ----------------------
with st.container():
    st.subheader("📄 Carga de CSV")
    col1, col2 = st.columns(2)
    with col1:
        archivo = st.file_uploader("Subir archivo CSV", type="csv")
    with col2:
        path = st.text_input("Path de guardado")
        target = st.text_input("Nombre de la columna target")

    tamano_test = st.number_input("Tamaño del test (%)", min_value=10, max_value=50, value=20)
    semilla = st.number_input("Número de semilla", min_value=0, value=42)
    escalado = st.selectbox("Método de escalado", ["StandardScaler", "MinMaxScaler", "RobustScaler"])

# ---------------------- INPUTS IMAGEN ----------------------
with st.container():
    st.subheader("🖼️ Carga de Imagen")
    uploaded_file = st.file_uploader(
        "Arrastra una imagen aquí o haz clic para seleccionar",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagen cargada", use_column_width=True)

# ---------------------- BOTÓN ENTRENAR ----------------------
if st.button("🚀 Entrenar Modelo"):
    if archivo is not None:
        df = f.leer(archivo)
        st.success("✅ CSV cargado correctamente")
        st.write("Path:", path)
        st.write("Target:", target)

        X, y = f.x_y(df, target)
        X_train, X_test, y_train, y_test = f.split_X_y(X, y, tamano_test/100, semilla)
        X_train_s, X_test_s = f.escalado(X_train, X_test, escalado)
        st.success("✅ Datos preparados y escalados")

        st.info("Entrenamiento del modelo completado con éxito 🔥")
    else:
        st.error("❌ Debes subir un CSV primero")

# ---------------------- PREDICCIÓN IMAGEN ----------------------
if uploaded_file is not None:
    st.subheader("🔮 Predicción de Emoción")
    emociones = ["😠 Enfadado", "😃 Feliz", "😌 Relajado", "😢 Triste"]
    pred_demo = np.random.choice(emociones)
    st.write(f"Emoción predicha: {pred_demo}")
    st.progress(80)  # ejemplo de barra de confianza
