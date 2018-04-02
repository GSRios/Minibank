from store.database import _db
from sqlalchemy.dialects.postgresql.base import UUID
_db.UUID = UUID
import uuid

class AccountModel(_db.Model):
    __tablename__ = 'account'

    id = _db.Column(_db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    
    client_id = _db.Column(_db.UUID(as_uuid=True), _db.ForeignKey('client.id'))   
    client = _db.relationship('ClientModel')
    
    
    def __init__(self, account):     
       self.id = account._id
       self.client_id = account.client_id

    def save(self):
        _db.session.add(self)
        _db.session.commit()
    
    @classmethod
    def get(cls, account_id):
        return cls.query.filter_by(id=account_id).first()