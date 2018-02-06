from domain.composite import Composite
from clientJoinedEvent import JoinedClientEvent
import datetime

class Client(Composite):
    def __init__(self, iden, name, email):
        super(Client, self).__init__(iden, [])
        self.__name = name
        self.__email = email
        self._events.append(JoinedClientEvent(iden, datetime.datetime.utcnow(), self.get_sequence(), self.__name, self.__email))
