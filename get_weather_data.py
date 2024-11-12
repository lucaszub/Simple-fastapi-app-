import requests

KEY = "673f5bbe15b1a94a502550359930545f"


def get_weather_by_city(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Non-success status code: {response.status_code}")
   
city = "Nantes"
test = get_weather_by_city(city)
print(test)




