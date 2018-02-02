import unittest
from app import app
from service import ClientService

class ClientTest(unittest.TestCase):
   
    def setUp(self):
        self.app = app.test_client()
        client_service = ClientService()
        command = {
            'name' : 'aa',
            'email' : 'aa@aa.com'
        }                
        self.client = client_service.process_new_client(command)
        self.response = self.app.get('/client/{}'.format(self.client.id)) 
        

    def test_get_client(self):         
        self.assertEqual(200, self.response.status_code) 

    def test_get_client_not_found(self): 
        response = self.app.get('/client/{}'.format('inexisting_client'))  
        self.assertEqual(404, response.status_code)         

    def test_post_client(self):       
        response = self.app.post('/client',
            data=dict(
                name='Test',
                email='t@t.com'
            ),follow_redirects=True )            
        self.assertEqual(201, response.status_code) 

    def test_post_client_with_error(self):       
        response = self.app.post('/client',
            data=dict(
                namae='Test',
                email='t@t.com'
            ),follow_redirects=True )            
        self.assertEqual(400, response.status_code)             
 
if __name__ == '__main__':
    unittest.main()
