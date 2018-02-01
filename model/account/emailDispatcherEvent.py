from domain import Event
from datetime import datetime

class DispatcherEmailEvent(Event):
    def __init__(self, accountID, sequence, sent_at):
        super(DispatcherEmailEvent, self).__init__(accountID, sent_at, sequence)