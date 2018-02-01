from store import MemoryStore

class Composite(object):
    def __init__(self, id, events):
        self.id = id
        self.events = events

    #Need to implement a lamport timestamp or vector clock
    def get_sequence(self):
        MemoryStore.lamport_timestamp = max(MemoryStore.lamport_timestamp, len(self.events))+1
        return MemoryStore.lamport_timestamp
