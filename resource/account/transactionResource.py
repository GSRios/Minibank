from flask_restful import Resource, reqparse
from flask import jsonify
from model.account.account import Account
from service import AccountNotFoundException, AccountService
from projection.transactionProjection import TransactionProjection

class TransactionResource(Resource):
    
    def __init__(self):
        super(TransactionResource, self).__init__()
        self.__service = AccountService()

    def get(self, accountID):
        try:            
            account = self.__service.get_account(accountID)
            transaction_projection = TransactionProjection(account)
        except AccountNotFoundException as account_not_found:
            return {'Message': str(account_not_found)}, 404

        return jsonify(transaction_projection.projection)
