from store.database import _db
from sqlalchemy.dialects.postgresql.base import UUID
_db.UUID = UUID
import uuid
import datetime

class EventModel(_db.Model):

    __tablename__ = "event"

    track_id = _db.Column(_db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    timestamp = _db.Column(_db.DateTime, default=datetime.datetime.utcnow ,nullable=False)
    sequence = _db.Column(_db.Integer, nullable=False)   
    type_event = _db.Column(_db.String(70), nullable=False)
    
    def __init__(self, id, timestamp, sequence, type_event):
        self.track_id = id
        self.timestamp = timestamp
        self.sequence = sequence
        self.type_event = type_event

    def save(self):        
        _db.session.add(self)
        _db.session.commit()
    
    @classmethod
    def get(cls, track_id):
        return cls.query.filter_by(id=track_id).first()

