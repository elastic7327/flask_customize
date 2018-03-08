# -*- coding: utf-8 -*-

import pytest

from src.models.models import User
from src.tests.base import BaseTestCase

from src.flaskr import app, db

from sqlalchemy import exc

from mixer.backend.flask import mixer

class TestSimpleModels(BaseTestCase):

    def test_simple_mixer_test(self):
        ran_user = mixer.blend(User)
        spec_user = mixer.blend(User, username="daniel", email="elastic7327@gamil.com")

        assert User.query.count() == 2

    def test_create_fake_users(self):
        user = mixer.blend(User)

        assert User.query.all()  is not None
        assert User.query.count() is not 0

    @pytest.mark.skip(reason="skip it for a moment")
    def test_create_fake_user_and_unique_fields(self):
        try:
            user_one = mixer.blend(User, username="daniel")
            user_two = mixer.blend(User, username="daniel")

        except exc.IntegrityError as e:

            db.session().rollback()

    def test_create_ten_fake_users(self):
        for n in range(10):
            mixer.blend(User)
        assert User.query.count() == 10

    def test_is_auto_deleted(self):
        assert User.query.count() is 0

