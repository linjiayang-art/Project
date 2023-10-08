import unittest
from backend import create_app
from backend.core.extensions import db
from flask import url_for
from backend.models.system import UserInfo

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        app=create_app('testing')
        self.context=app.test_request_context()
        self.context.push()
        self.client=app.test_client()
        self.runner=app.test_cli_runner()

        db.create_all()
        user=UserInfo(userno='666',username='linyang',password='123')
        db.session.add(user)
        db.session.commit()
    
    def tearDown(self):
        db.drop_all()
        self.context.pop()

    def login(self,username=None,password=None):
        if username is None and password is None:
            username='linyang'
            password='123'

        return self.client.post(
            url_for('auth.login'),
            data=dict(username=username,password=password),
            follow_redirects=True
            )
    