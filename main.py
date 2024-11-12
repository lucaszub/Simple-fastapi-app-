from fastapi import FastAPI
import uvicorn
from get_weather_data import get_weather_by_city 


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/wether_data")
def get_weather_data(city):
    weather_by_city = get_weather_by_city(city)
    return { "Température pour votre ville" : weather_by_city}
