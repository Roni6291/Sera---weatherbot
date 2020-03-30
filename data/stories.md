## story001
* greet
    - utter_greet
* fine_ask
    - utter_reply
* inform
    - utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - action_weather
    - slot{"location": "paris"}
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye


## story002
* greet
    - utter_greet
* fine_ask
    - utter_reply
* inform
    - utter_ask_location
* inform{"location": "moscow"}
    - slot{"location": "moscow"}
    - action_temperature
    - slot{"location": "moscow"}
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye


## story003
* greet
    - utter_greet
* fine_normal
    - utter_help
* inform
    - utter_ask_location
* inform{"location": "sydney"}
    - slot{"location": "sydney"}
    - action_temperature
    - slot{"location": "sydney"}
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye


## story004
* greet
    - utter_greet
* fine_normal
    - utter_help
* inform
    - utter_ask_location
* inform{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_weather
    - slot{"location": "mumbai"}
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye


## story005
* greet
    - utter_greet
* fine_ask
    - utter_reply
* inform{"location": "new york"}
    - slot{"location": "new york"}
    - action_weather
    - slot{"location": "new york"}
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye


## story006
* greet
    - utter_greet
* fine_ask
    - utter_reply
* inform{"location": "oslo"}
    - slot{"location": "oslo"}
    - action_temperature
    - slot{"location": "oslo"}
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye


## story007
* greet
    - utter_greet
* fine_normal
    - utter_help
* inform{"location": "london"}
    - slot{"location": "london"}
    - action_temperature
    - slot{"location": "london"}
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye


## story008
* greet
    - utter_greet
* fine_normal
    - utter_help
* inform{"location": "amsterdam"}
    - slot{"location": "amsterdam"}
    - action_weather
    - slot{"location": "amsterdam"}
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye
