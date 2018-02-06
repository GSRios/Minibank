from resource import DepositAccountResource, WithdrawAccountResource, TransactionResource, AccountResource, ClientResource
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

api.add_resource(ClientResource, '/client', endpoint='clients')
api.add_resource(ClientResource, '/client/<string:id>', endpoint='client')

api.add_resource(AccountResource, '/account', endpoint='accounts')
api.add_resource(AccountResource, '/account/<string:id>', endpoint='account')
api.add_resource(DepositAccountResource, '/account/<string:accountID>/deposit')
api.add_resource(WithdrawAccountResource, '/account/<string:accountID>/withdraw')
api.add_resource(TransactionResource, '/account/<string:accountID>/history')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Ab123456@localhost/minibank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_tables():
    _db.create_all

if __name__ == '__main__':
    from store.database import _db
    _db.init_app(app)
    app.run(port=5000)