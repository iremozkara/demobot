# # # This files contains your custom actions which can be used to run
# # # custom Python code.
# # #
# # # See this guide on how to implement these action:
# # # https://rasa.com/docs/rasa/custom-actions


# # # This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
# from weather import Weather
import webbrowser
# from rasa_sdk.types import DomainDict

import datetime
import calendar
import requests as r
api = "http://api.weatherapi.com/v1/current.json"
api_key = "4f37efb32b2648f59c7112325210308"

class ActionVideo(Action):
	def name(self) -> Text:
		return "action_video"

	async def run(self,dispatcher,tracker:Tracker,domain:"DomainDict",
		) ->List[Dict[Text,Any]]:
			video_url = "https://www.youtube.com/watch?v=KPJJZHjevtk"
			dispatcher.utter_message("Please Wait, I will play the video soon...")
			webbrowser.open(video_url)
			return[]


# # class ValidateNameForm(FormValidationAction):
# # 	def name(self) -> Text:
# # 		return "validate_name_form"
# # 	def validate_first_name(
# # 		self,
# # 		slot_value:Any,
# # 		dispatcher: CollectingDispatcher,
# # 		tracker: Tracker,
# # 		domain: DomainDict,
# # 	) -> Dict[Text, Any]:


# # #



# class RequestAction(Action):

#     def name(self) -> Text:
    	
#         return "action_weather_api"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#     	city=tracker.latest_message.get('text')
#     	temp = Weather(city)
#     	dispatcher.utter_template("utter_temp",tracker,temp=temp)

#     		# first_name = tracker.get_slot("first_name")
#     		# last_name = tracker.get_slot("last_name")
#     		# address = tracker.get_slot("address")

#     		# if first_name is not None and last_name is not None and address is not None:
#     		# 	dispatcher.utter_message(text = "All info is gathered! ")
#     		# else:
#     		# 	dispatcher.utter_message(text="Fail")

#         return []


# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionTellTime(Action):

    def name(self) -> Text:
        return "tell_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        myTime = datetime.datetime.now()

        dispatcher.utter_message(text="It's %s:%s" % (myTime.hour, myTime.minute))

        return []

class ActionTellDate(Action):

    def name(self) -> Text:
        return "tell_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        myTime = datetime.datetime.now()
        theDay = calendar.day_name[myTime.weekday()]

        dispatcher.utter_message(text="Today is %s %s/%s/%s" % (theDay,myTime.day, myTime.month, myTime.year))

        return []

class ActionTellWeather(Action):

    def name(self) -> Text:
    	return "tell_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        def currentTemp(location, aqi = "no"):
            response = r.get(api , params = {"key": api_key, "q": location, "aqi": aqi})
            response.encoding = 'utf-8'
            data = response.json()
            return data["current"]["temp_c"], data["current"]["condition"]["text"]

        myWeather, condition = currentTemp("Istanbul")
        dispatcher.utter_message(text="Its %s degrees and the weather is %s" % (myWeather,condition))
        return []