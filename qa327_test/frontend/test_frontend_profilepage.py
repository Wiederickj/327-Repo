import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend homepage.
"""

#sample user
new_test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_Frontend0!')
)

#testing frontend user profile page
class UserProfilePageTestFrontEnd(BaseCase):

    @patch('qa327.backend.get_user', return_value=new_test_user)
    
    #test R3.1
    def test_logged_out(self, *_):

        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
        
    #test R3.2
    def test_hi_header(self, *_):
        
        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
        
        #enter email and password of test_user into #email and #password elements
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        
        # click login button
        self.click('input[type="submit"]')
        
        # open home page
        self.open(base_url)
        
        #validate  welcome-header element outputs correct phrase
        self.assert_element("#welcome-header")
        self.assert_text("Hi test_frontend", "#welcome-header")
        
    def #test R3.3
        
