import unittest
from backend import create_app
from backend.core.extensions import db
from flask import url_for
from backend.models.system import UserInfo


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app('testing')
        self.context = app.test_request_context()
        self.context.push()
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

        db.create_all()
        user = UserInfo(userno='666', username='linyang', password='123')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        self.context.pop()

    def login(self, username=None, password=None):
        if username is None and password is None:
            userno = '666'
            password = '123'

        return self.client.post(
            url_for('api_v1.token'),
            data=dict(userno=userno, password=password),
            follow_redirects=True
        )

    def get_oauth_token(self):
        response = self.client.post(url_for('api_v1.token'), json=dict(
                userno='666', 
                password='123'
        ),follow_redirects=True)
        data = response.get_json()

        return data['data']['access_token']

    def set_auth_headers(self, token):
        return {
            'Authorization': 'Bearer'+token,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
