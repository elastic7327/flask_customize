
from src.flaskr import app, db
from mixer.backend.flask import mixer

import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # get test-config
        app.config.from_object('src.configs.settings.TestingConfig')
        app.config['TESTING'] = True

        # init mixer
        mixer.init_app(app)
        self.client = app.test_client()

        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
