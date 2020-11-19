import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url


# integration testing:

@pytest.mark.usefixtures('server')
class Registered(BaseCase):

    def register(self):
        #register new user
        self.open(base_url + '/register')
        self.type("#email", "test_integration@test.com")
        self.type("#name", "test0")
        self.type("#password", "Test0!qwertyuiop")
        self.type("#password2", "Test0!qwertyuiop")
        self.click('input[type="submit"]')

    def login(self):
        # Login and verify that login was successful.
        self.open(base_url + '/login')
        self.type("#email", "test_integration@test.com")
        self.type("#password", "Test0!qwertyuiop")
        self.click('input[type="submit"]')

    def test_register_login(self):
        #This test checks the implemented login/logout feature
        self.register()
        self.login()
        self.open(base_url)
        self.assert_element("#welcome-header")
        #self.assert_text("Welcome test0", "#welcome-header")

        