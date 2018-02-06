class Event(object):
    def __init__(self, compositeID, timestamp, sequence):
        self._compositeID = compositeID
        self._timestamp = timestamp
        self._sequence = sequence
