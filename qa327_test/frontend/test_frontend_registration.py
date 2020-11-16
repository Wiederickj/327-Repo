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

# Moch some sample tickets
new_test_tickets = [
    {'name': 't1', 'price': '150'}
]

#Test R1.1
class HomePageTestFrontEnd(BaseCase):

    @patch('qa327.backend.get_user', return_value=new_test_user)
    @patch('qa327.backend.get_all_tickets', return_value=new_test_tickets)
    def test_login_success(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open login page
        self.open(base_url + '/login')
        # fill in the correct email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        # click enter button
        self.click('input[type="submit"]')
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome test_frontend", "#welcome-header")
        self.assert_element("#tickets div h4")
        self.assert_text("t1 150", "#tickets div h4")


#Test R1 For any formatting errors, render the login page and show the message 'email/password format is incorrect.'

    @patch('qa327.backend.get_user', return_value=new_test_user)
    @patch('qa327.backend.get_all_tickets', return_value=new_test_tickets)
    
    def test_login_password_failed(self, *_):
        # open login page
        self.open(base_url + '/login')
        # Enter the wrong email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "wrong_passworD!0")
        # click enter button
        self.click('input[type="submit"]')
        # make sure that the proper error message shows up
        self.assert_element("#message")
        self.assert_text("login failed", "#message")
