import streamlit as st
from plant_model import predict_plant_stress

st.set_page_config(
    page_title="RootMind",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 RootMind")
st.subheader("Smart Plant Health Monitoring System")

st.write(
    "Monitor plant conditions and identify "
    "possible plant stress."
)

st.header("Enter Plant Sensor Readings")

soil = st.slider("Soil Moisture (%)", 0, 100, 50)
temperature = st.slider("Temperature (°C)", 0, 50, 25)
humidity = st.slider("Air Humidity (%)", 0, 100, 60)

if st.button("Predict Plant Health"):
    result = predict_plant_stress(
        soil, temperature, humidity
    )

    st.subheader("Prediction Result")
    st.success(result)

st.caption("RootMind | Smart Agriculture")