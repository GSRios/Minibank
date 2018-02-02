from store import Connection

class EventDAO(Connection):
    def __init__(self):
        super(EventDAO, self).__init__()


    def get_events(self, trackID):
        pass
    
    def save_events(self, events):
        pass
