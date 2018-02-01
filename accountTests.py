import unittest
from app import app

class ClientTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_account(self):
        url = self.test_post_account(True)
        response = self.app.get(url)  
        self.assertEqual(200, response.status_code)      

    def test_post_account(self, need_return=False):       
        response = self.app.post('/client',
            data=dict(
                clientID='aaa'
            ),follow_redirects=True )            
        self.assertEqual(201, response.status_code)
        if need_return:
            url = response.data.decode('utf-8').replace("\"", "").strip()           
            return url
 
if __name__ == '__main__':
    unittest.main()
