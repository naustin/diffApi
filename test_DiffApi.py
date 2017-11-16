import diffApi
import unittest 

class DiffApiTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        # creates a test client
        self.diffApi = diffApi.test_client()
        # propagate the exceptions to the test client
        self.diffApi.testing = True 

    def tearDown(self):
        pass 

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.diffApi.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.diffApi.get('/') 

        # assert the response data
        self.assertEqual(result.data, "Hello!")
