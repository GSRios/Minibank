from domain.event import Event

class JoinedClientEvent(Event):
    def __init__(self, id, timestamp, sequence, name, email):    
        super(JoinedClientEvent, self).__init__(id, timestamp, sequence)
        self.name = name
        self.email = email
