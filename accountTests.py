import unittest
from app import app
from service import ClientService, AccountService, AccountNotFoundException, ClientNotFoundException

class ClientTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
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
        self.assertEqual(200, self.response.status_code)      

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

    def test_withdraw(self):
        pass

    def test_deposit(self):
        pass

 
if __name__ == '__main__':
    unittest.main()
