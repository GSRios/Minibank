from domain.composite import Composite
from clientJoinedEvent import JoinedClientEvent
import datetime

class Client(Composite):
    def __init__(self, iden, name, email):
        super(Client, self).__init__(iden, [])
        self._name = name
        self._email = email
        new_client_event = JoinedClientEvent(iden, datetime.datetime.utcnow(), self.get_sequence())
        self._events.append(new_client_event)
