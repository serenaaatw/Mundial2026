import requests
from config.config import config_clima

def obtener_clima(lat, lon):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}"
        f"&lon={lon}"
        f"&appid={config_clima.OPENWEATHER_API_KEY}"
        "&units=metric"
        "&lang=es"
    )
    respuesta = requests.get(url)
    return respuesta.json()