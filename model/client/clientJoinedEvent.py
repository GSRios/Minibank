from domain.event import Event

class JoinedClientEvent(Event):
    def __init__(self, id, timestamp, sequence):    
        super(JoinedClientEvent, self).__init__(id, timestamp, sequence)        
