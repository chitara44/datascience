class SubscribeUser(Action):
    def name(self):
        return "subscribe_user"
    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        subscribe = tracker.get_slot('subscribe')
        if subscribe == “True”:
        response = "You're successfully subscribed"
        if subscribe == “False”:
        response = "You're successfully unsubscribed"
        dispatcher.utter_message(response)
        return [SlotSet("subscribe", subscribe)]