def predict_plant_stress(soil, temperature, humidity):

    if soil < 25:
        return "Water Stress Detected! Plant needs water."

    elif temperature > 38:
        return "Heat Stress Detected! Temperature is high."

    elif humidity < 25:
        return "Low Humidity Stress Detected."

    elif soil < 40:
        return "Warning: Soil moisture is getting low."

    else:
        return "Plant conditions appear normal."