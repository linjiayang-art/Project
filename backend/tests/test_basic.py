from flask import current_app

from .base import BaseTestCase

class BasicTestCase(BaseTestCase):


    def test_app_exist(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_404_error(self):
        response=self.client.get('/api/foo')
        data=response.get_json()
        self.assertEqual(response.status_code,404)
        self.assertIn( 'The requested URL was not found on the server.',data['msg'])

    '''def test_401_error(self):
        response=self.client.get('/foo')
        data=response.get_data(as_text=True)
        self.assertEqual(response.status_code,401)
        print(data)
        self.assertIn(  data['msg'],'The requested URL was not found on the server.')'''
        