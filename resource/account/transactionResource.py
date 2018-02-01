from flask_restful import Resource, reqparse
from flask import jsonify
from model.account.account import Account
from service.account import AccountService
from service import AccountNotFoundException
from projection.transactionProjection import TransactionProjection

class TransactionResource(Resource):
    global account_service
    account_service = AccountService()

    def get(self, accountID):
        try:            
            account = account_service.get_account(accountID)
            transaction_projection = TransactionProjection(account)
        except AccountNotFoundException as account_not_found:
            return {'Message': str(account_not_found)}, 404

        return jsonify(transaction_projection.projection)
