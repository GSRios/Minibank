import unittest
from app import app as application
from service import ClientService
from service import AccountService
from service import AccountNotFoundException
from service import ClientNotFoundException

class ClientTest(unittest.TestCase):

    def setUp(self):
        self.app = application.test_client()
        client_service = ClientService()
        account_service = AccountService()
        command = {
            'name' : 'aa',
            'email' : 'aa@aa.com'
        }                
        self.client = client_service.process_new_client(command)
        self.account = account_service.proccess_new_account(str(self.client.id))
        self.response = self.app.get('/account/{}'.format(self.account.id))

    def test_get_account(self): 
        """Method to test get an account"""
        self.assertEqual(200, self.response.status_code)

    def test_get_account_not_found(self): 
        """Method to test get an account not existing"""               
        response = self.app.get('/account/{}'.format('inexisting_account'))      
        self.assertEqual(404, response.status_code)   

    def test_post_account(self):       
        response = self.app.post('/account',
            data=dict(
                clientID=str(self.client.id)
            ),follow_redirects=True )            
        self.assertEqual(201, response.status_code)

    def test_post_account_client_not_found(self):       
        response = self.app.post('/account',
            data=dict(
                clientID='inexisting_client'
            ),follow_redirects=True )            
        self.assertEqual(404, response.status_code)   

    def test_withdraw_without_balance(self):
        response = self.app.post('/account/{}/withdraw'.format(str(self.account.id)),
            data=dict(amount= 10000.00)
        , follow_redirects=True)
        self.assertEqual(403, response.status_code)

    def test_withdraw(self):
        self.test_deposit()
        response = self.app.post('/account/{}/withdraw'.format(str(self.account.id)),
            data=dict(amount= 1000.00)
        , follow_redirects=True)
        self.assertEqual(200, response.status_code)

    def test_deposit(self):
        response = self.app.post('/account/{}/deposit'.format(str(self.account.id)),
            data=dict(amount= 1000.00)
        , follow_redirects=True)
        self.assertEqual(200, response.status_code)

    def test_transactions(self):
        response = self.app.get('/account/{}/history'.format(str(self.account.id)))        
        self.assertEqual(200, response.status_code)

 
if __name__ == '__main__':
    unittest.main()
