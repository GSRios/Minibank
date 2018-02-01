from domain.event import Event

class JoinedClientEvent(Event):
    def __init__(self, id, timestamp, version, name, email):    
        super(JoinedClientEvent, self).__init__(id, timestamp, version)
        self.name = name
        self.email = email
