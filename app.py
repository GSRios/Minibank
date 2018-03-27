from flask import Flask
from flask_restful import Resource, Api
from resource import DepositAccountResource
from resource import WithdrawAccountResource
from resource import TransactionResource
from resource import AccountResource
from resource import ClientResource
from store.database import _db


app = Flask(__name__)
api = Api(app)

api.add_resource(ClientResource, '/client', endpoint='clients')
api.add_resource(ClientResource, '/client/<string:id>', endpoint='client')

api.add_resource(AccountResource, '/account', endpoint='accounts')
api.add_resource(AccountResource, '/account/<string:id>', endpoint='account')
api.add_resource(DepositAccountResource, '/account/<string:accountID>/deposit')
api.add_resource(WithdrawAccountResource, '/account/<string:accountID>/withdraw')
api.add_resource(TransactionResource, '/account/<string:accountID>/history')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:za3o5p4r@localhost/minibank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_tables():
    _db.create_all()
   

if __name__ == '__main__':  
    _db.init_app(app)
    app.run(port=5000)