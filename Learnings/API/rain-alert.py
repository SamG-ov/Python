import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key="07e1aec44f19ad300bd059232982e7b3"
account_sid = "S14EUT1ZBW47TS45UYQH4ZT3"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"


weather_params = {
    "lat": 51.048615,
    "lon": -114.070847,
    "appid": api_key,
    "cnt":4,
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)