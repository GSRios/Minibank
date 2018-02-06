from store import MemoryStore

    def __init__(self, id, events):
class Composite(object):
        self._id = id
        self._events = events

    #Need to implement a lamport timestamp or vector clock
    def get_sequence(self):
        MemoryStore.lamport_timestamp = max(MemoryStore.lamport_timestamp, len(self._events))+1
        return MemoryStore.lamport_timestamp
