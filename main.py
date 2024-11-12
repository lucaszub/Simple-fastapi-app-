from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/wether_data")
def get_weather_data():
    return { "Nantes" : "24°"}
