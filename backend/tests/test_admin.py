from .base import BaseTestCase
from backend.models.system import UserInfo
from backend.core.extensions import db 
from flask import url_for
class AdminTestCase(BaseTestCase):
    def setUp(self):
        super(AdminTestCase,self).setUp()
        self.login()
        #return super(AdminTestCase,self)
        return super().setUp()
    
    def test_api_index(self):
        response=self.client.get(url_for('api_v1.index'))
        data=response.get_json()
        self.assertEqual(data['api_version'],'1.0')
        self.get_oauth_token()

    def test_get_menus(self):
        pass