from domain import Event

class DepositEvent(Event):
    def __init__(self, trackID, timestamp, sequence, amount):
        super(DepositEvent, self).__init__(trackID, timestamp, sequence)
        self.amount = amount        

class WithdrawEvent(Event):
    def __init__(self, trackID, timestamp, sequence, amount):
        super(WithdrawEvent, self).__init__(trackID, timestamp, sequence)
        self.amount = amount       


class AccountOpenedEvent(Event):
    def __init__(self, trackID, timestamp, sequence, clientUUID):
        super(AccountOpenedEvent, self).__init__(trackID, timestamp, sequence)
        self.clientID = clientUUID        