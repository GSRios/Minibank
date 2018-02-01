class Event(object):
    def __init__(self, aggregateUUID, timestamp, version):
        self.aggregateUUID = aggregateUUID
        self.timestamp = timestamp
        self.version = version
