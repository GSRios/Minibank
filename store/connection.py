import psycopg2

class Connection(object):
    _db=None
    def __init__(self):
        self._db = psycopg2.connect(host='localhost', database='db', user='usr', password='pwd')