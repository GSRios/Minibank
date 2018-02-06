from store.database import _db
import uuid

class AccountModel(_db.Model):
    __tablename__ = 'account'

    id = _db.Column(_db.UUID(as_uuid=True), default=uuid.uuid4(), primary_key=True)
    client_id = _db.Column(_db.UUID(as_uuid=True), _db.ForeignKey('client.id'))
    client = _db.relationship('ClientModel')
    
    def __init__(self):
       pass

    def save_account(self, account):
        pass
    
    def get_account(self, accoutID):
        pass