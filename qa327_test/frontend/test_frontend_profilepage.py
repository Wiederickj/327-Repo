import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend homepage.
"""

#Sample user
new_test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_Frontend0!')
)

class LogInPageTestFrontEnd(BaseCase):

    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_logged_out(self, *_):

        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
