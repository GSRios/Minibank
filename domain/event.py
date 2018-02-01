class Event(object):
    def __init__(self, compositeUUID, timestamp, version):
        self.compositeUUID = compositeUUID
        self.timestamp = timestamp
        self.version = version
