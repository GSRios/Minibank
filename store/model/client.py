from store.database import _db
from sqlalchemy.dialects.postgresql.base import UUID
_db.UUID = UUID
import uuid

class ClientModel(_db.Model):

    __tablename__ = "client"

    id = _db.Column(_db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    name = _db.Column(_db.String(80), nullable=False)
    email = _db.Column(_db.String(100), nullable=False)    
    
    accounts = _db.relationship('AccountModel', lazy='dynamic')

    
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def save(self):        
        _db.session.add(self)
        _db.session.commit()
    
    @classmethod
    def get(cls, clientID):
        return cls.query.filter_by(id=clientID).first()

