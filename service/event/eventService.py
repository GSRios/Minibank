from store import EventModel

class EventService(object):

    @classmethod
    def save(cls, events):
        for event in events:
            event_model = EventModel(event)
            event_model.save()