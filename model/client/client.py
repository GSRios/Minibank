from domain.composite import Composite
from clientJoinedEvent import JoinedClientEvent
import datetime

class Client(Composite):
    def __init__(self, iden, name, email):
        super(Client, self).__init__(iden, [])
        self.id = iden
        self.name = name
        self.email = email
        self.events.append(JoinedClientEvent(iden, datetime.datetime.utcnow(), self.get_sequence(), name, email))
