class Composite(object):
    def __init__(self, id, events):
        self.id = id
        self.events = events

    #Need to implement a lamport timestamp or vector clock
    def get_sequence(self):
        #t = max(t, len(self.events))+1
        return len(self.events) +1
