import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Abdomen de Acero", page_icon="💪")

st.title("🔥 Rutina de Abdomen")
st.write("Mantén la constancia para ver resultados.")

# Datos de la rutina
ejercicios = {
    "1. Plancha (Plank)": {
        "video": "https://www.youtube.com/watch?v=ASdvN_XEl_c",
        "desc": "Mantén el cuerpo como una tabla. No bajes la cadera.",
        "tiempo": 45
    },
    "2. Deadbug": {
        "video": "https://www.youtube.com/watch?v=4XLEnwUr1d8",
        "desc": "Espalda baja pegada al suelo. Movimiento lento.",
        "tiempo": 60
    },
    "3. Elevación de Piernas": {
        "video": "https://www.youtube.com/watch?v=JB2oyawG9KI",
        "desc": "Baja lento sin tocar el suelo. Controla la subida.",
        "tiempo": 45
    },
    "4. Bicycle Crunches": {
        "video": "https://www.youtube.com/watch?v=9FGilxCbdz8",
        "desc": "Gira el torso, hombro a rodilla contraria.",
        "tiempo": 45
    },
    "5. Plancha Lateral": {
        "video": "https://www.youtube.com/watch?v=_bDD8osA7uU",
        "desc": "Codo bajo el hombro. Sube la cadera.",
        "tiempo": 30
    }
}

# Selección del ejercicio
opcion = st.selectbox("Selecciona el ejercicio:", list(ejercicios.keys()))
datos = ejercicios[opcion]

# Mostrar información
st.header(opcion)
st.info(datos["desc"])
st.video(datos["video"])

# Cronómetro integrado
st.write("---")
st.subheader(f"⏱️ Temporizador: {datos['tiempo']} segundos")

if st.button("Iniciar Serie"):
    barra = st.progress(0)
    conteo = st.empty()
    
    for i in range(datos["tiempo"] + 1):
        conteo.metric("Tiempo restante", f"{datos['tiempo'] - i} s")
        barra.progress(i / datos["tiempo"])
        time.sleep(1)
    
    st.success("¡Serie completada! Descansa 15 segundos.")
    st.balloons()
