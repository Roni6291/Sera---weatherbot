import requests
import pprint

pp = pprint.PrettyPrinter()
access_key = "2225fa89402411623da4dd2be345b507"

if __name__ == "__main__":
        params = {
                  "appid": access_key,
                  "units": "metric",
                  "q": "Moscow"
                }

        api_result = requests.get("http://api.openweathermap.org/data/2.5/weather", params)

        api_response = api_result.json()

        # city = api_response["location"]["name"]
        # condition = api_response["current"]["condition"]["text"]
        # temp_c = api_response["current"]["temp_c"]
        # wind_speed = api_response["current"]["wind_mph"]
        # humidity = api_response["current"]["humidity"]

        # response = """It is currently {} in {} at the moment. The temperature is {} degrees, the relative humidity is {}
        #          percent. The wind speed  is {} mph""".format(condition, city, temp_c, humidity, wind_speed)


        pp.pprint(api_response)
