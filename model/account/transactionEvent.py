from domain import Event

class DepositEvent(Event):
    def __init__(self, track_id, timestamp, sequence, amount):
        super(DepositEvent, self).__init__(track_id, timestamp, sequence)
        self.amount = amount        

class WithdrawEvent(Event):
    def __init__(self, track_id, timestamp, sequence, amount):
        super(WithdrawEvent, self).__init__(track_id, timestamp, sequence)
        self.amount = amount       

class AccountOpenedEvent(Event):
    def __init__(self, track_id, timestamp, sequence):
        super(AccountOpenedEvent, self).__init__(track_id, timestamp, sequence)   