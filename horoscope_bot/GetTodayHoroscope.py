from rasa_core.actions import Action
from rasa_core.events import SlotSet
class GetTodaysHoroscope(Action):
    def name(self):
        return "get_todays_horoscope"
    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        user_horoscope_sign = tracker.get_slot('horoscope_sign')
        """Write your logic to get today’s horoscope details
        for the given Horoscope sign based on some API calls
        or retrieval from the database"""
        return [SlotSet("horoscope_sign", user_horoscope_sign)]