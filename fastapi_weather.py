from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "b30ec4afba2a5fd167bf1d19f2e96551"


@app.get("/weather")
def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return {
        "test":"First Api call",
        "city": city,        
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"]
    }
