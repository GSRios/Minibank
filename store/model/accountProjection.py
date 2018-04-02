from store.database import _db
from sqlalchemy.dialects.postgresql.base import UUID
_db.UUID = UUID
import uuid

class AccountProjectionModel(_db.Model):
    __tablename__ = 'account_projection'
    
    account_id = _db.Column(_db.UUID(as_uuid=True),  _db.ForeignKey('account.id'), default=uuid.uuid4, primary_key=True)
    balance = _db.Column(_db.Float(13,2), nullable=False, default=0)
    account = _db.relationship('AccountModel')

    def __init__(self, account_id, new_balance):
        self.account_id = account_id
        self.balance = new_balance
        

    def save(self):
        _db.session.add(self)
        _db.session.commit()
    
    @classmethod
    def get(cls, account_id):
        return cls.query.filter_by(account_id=account_id).first()