from resource.account.accountResource import AccountResource
from resource.client.clientResource import ClientResource
from resource.account.depositResource import DepositAccountResource
from resource.account.withdrawResource import WithdrawAccountResource
from resource.account.transactionResource import TransactionResource
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

if __name__ == '__main__':
    app.run(port=5000)