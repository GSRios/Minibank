from flask_restful import Resource, reqparse
from flask import jsonify
from model.account.account import Account
from service import AccountNotFoundException
from projection.transactionProjection import TransactionProjection

class TransactionResource(Resource):
    
    def get(self, account_id):
        try:                       
            transaction_projection = TransactionProjection(account_id)
        except AccountNotFoundException as account_not_found:
            return {'Message': str(account_not_found)}, 404

        return jsonify(transaction_projection.projection)
