
import requests
import twilio
from twilio.rest import Client
OWN_END="https://api.openweathermap.org/data/2.5/forecast"
api_key="68db1d02bc08f0dea99af1e78b67b46f"
account_sid = 'your account_sid"
auth_token = 'your auth_token'
weather_params={
    "appid": api_key,
    "lat":17.385044,
    "lon":78.486671,
    'cnt':4
}
response=requests.get(OWN_END,params=weather_params)
response.raise_for_status()
weather_data=response.json()
print(weather_data)
will_rain=False
for hour_data in weather_data['list']:
    condition=hour_data['weather'][0]['id']
    if int(condition)<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12694619412',
        body='It is going to rain today,Bring Umberella!',
        to='+919390586610'
    )

    print(message.status)
