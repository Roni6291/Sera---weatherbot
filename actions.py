from rasa_core_sdk import Action
from rasa_core.events import SlotSet

import requests

class ActionWeather(Action):

    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        access_key = "2225fa89402411623da4dd2be345b507"
        loc = tracker.get_slot('location')

        params = {
                  "appid": access_key,
                  "units": "metric",
                  "q": loc
                }

        api_result = requests.get("http://api.openweathermap.org/data/2.5/weather", params)
        response = api_result.json()

        city = response["name"]
        condition = response["weather"][0]["description"]
        temp_c = response["main"]["temp"]
        wind_speed = response["wind"]["speed"]
        humidity = response["main"]["humidity"]

        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the relative humidity is {}
                 percent. The wind speed  is {} kmph""".format(condition, city, temp_c, humidity, wind_speed)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]


class ActionTemperature(Action):

    def name(self):
        return 'action_temperature'

    def run(self, dispatcher, tracker, domain):
        access_key = "2225fa89402411623da4dd2be345b507"
        loc = tracker.get_slot('location')

        params = {
                  "appid": access_key,
                  "units": "metric",
                  "q": loc
                }

        response = requests.get("http://api.openweathermap.org/data/2.5/weather", params)

        city = response["name"]
        temp_c = response["main"]["temp"]


        response = """It is currently {} degrees in {} at the moment""".format(temp_c, city)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]
