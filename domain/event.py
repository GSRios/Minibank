class Event(object):
    def __init__(self, composite_id, timestamp, sequence):
        self._composite_id = composite_id
        self._timestamp = timestamp
        self._sequence = sequence
