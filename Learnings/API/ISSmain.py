import requests
import datetime as dt

my_lat = 51.048615
my_lng = -114.070847

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    print(data)

    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    if my_lat-5 <= latitude <= my_lat+5 and my_lng-5 <= longitude <= my_lng+5:
        return True

def is_night():
    parameters = {
        "lat":my_lat,
        "lng":my_lng,
        "formatted": 0
    }
    response1 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response1.raise_for_status()

    data1 = response1.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    now = dt.datetime.now().hour

    if now >= sunset or now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    print("Yesss")