from store.database import _db
from sqlalchemy.dialects.postgresql.base import UUID
_db.UUID = UUID

class ClientModel(_db.Model):

    __tablename__ = "client"

    id = _db.Column(_db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    name = _db.Column(_db.String(80), nullable=False)
    email = _db.Column(_db.String(100), nullable=False)
    accounts = _db.relationship('AccountModel', lazy='dynamic')

    def __init__(self):
        super(ClientDAO, self).__init__()

    def save_client(self, client):
        pass
    
    def get_client(self, clientID):
        pass

