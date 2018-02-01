from domain import Event

class DepositEvent(Event):
    def __init__(self, trackID, timestamp, version, amount):
        super(DepositEvent, self).__init__(trackID, timestamp, version)
        self.amount = amount        

class WithdrawEvent(Event):
    def __init__(self, trackID, timestamp, version, amount):
        super(WithdrawEvent, self).__init__(trackID, timestamp, version)
        self.amount = amount       


class AccountOpenedEvent(Event):
    def __init__(self, eventUUID, timestamp, version, clientUUID):
        super(AccountOpenedEvent, self).__init__(eventUUID, timestamp, version)
        self.clientUUID = clientUUID        