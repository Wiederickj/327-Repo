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

class RegisterTest(BaseCase):

    def test_register_page(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter valid email
        self.type("#email", "test_registration@test.com")
        #enter valid Name
        self.type("#name", "testName")
        #enter matching passwords
        self.type("#password", "valid_Pass")
        self.type("#password2", "valid_Pass")
        self.click('input[type="submit"]')

    def test_email_fail(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter invalid email
        self.type("#email", "invalidEmail")
        #enter valid Name
        self.type("#name", "testName")
        #enter matching passwords
        self.type("#password", "valid_Pass")
        self.type("#password2", "valid_Pass")
        #Display proper error message 
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Email format error", "#message")

    def test_password_short(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter valid email
        self.type("#email", "test_registration@test.com")
        #enter valid Name
        self.type("#name", "testName")
        #enter too short password
        self.type("#password", "short")
        self.type("#password2", "short")
        #Display proper error message 
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Password not strong enough", "#message")

    def test_password_Cap(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter valid email
        self.type("#email", "test_registration@test.com")
        #enter valid Name
        self.type("#name", "testName")
        #enter matching passwords
        self.type("#password", "test_pass")
        self.type("#password2", "test_pass")
        #Display proper error message 
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Password not strong enough", "#message")

    def test_password_All_Cap(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter valid email
        self.type("#email", "test_registration@test.com")
        #enter valid Name
        self.type("#name", "testName")
        #enter matching passwords
        self.type("#password", "TEST_PASS")
        self.type("#password2", "TEST_PASS")
        #Display proper error message 
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Password not strong enough", "#message")\

    def test_password_no_special(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter valid email
        self.type("#email", "test_registration@test.com")
        #enter valid Name
        self.type("#name", "testName")
        #enter matching passwords
        self.type("#password", "testPass")
        self.type("#password2", "testPass")
        #Display proper error message 
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Password not strong enough", "#message")

    def test_password_fail(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter valid email
        self.type("#email", "test_registration@test.com")
        #enter valid Name
        self.type("#name", "testName")
        #enter non matching passwords
        self.type("#password", "valid_Pass")
        self.type("#password2", "wrong_Pass")
        #Display proper error message 
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_name_fail(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter valid email
        self.type("#email", "test_registration@test.com")
        #enter invalid Name
        self.type("#name", "name@test")
        #enter matching passwords
        self.type("#password", "valid_Pass")
        self.type("#password2", "valid_Pass")
        #Display proper error message 
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Username not allowed", "#message")

    def test_name_space(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter valid email
        self.type("#email", "test_registration@test.com")
        #enter invalid Name
        self.type("#name", " nametest")
        #enter matching passwords
        self.type("#password", "valid_Pass")
        self.type("#password2", "valid_Pass")
        #Display proper error message 
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Username not allowed", "#message")

    def test_name_short(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter valid email
        self.type("#email", "test_reg3@test.com")
        #enter valid Name
        self.type("#name", "A")
        #enter matching passwords
        self.type("#password", "valid_Pass")
        self.type("#password2", "valid_Pass")
        #Display proper error message 
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Username not allowed", "#message")

    def test_name_long(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter valid email
        self.type("#email", "test_registration@test.com")
        #enter valid Name
        self.type("#name", "UsernameIsMoreThan20Characters")
        #enter matching passwords
        self.type("#password", "valid_Pass")
        self.type("#password2", "valid_Pass")
        #Display proper error message 
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Username not allowed", "#message")

    def test_email_used(self, *_):
        #open register page
        self.open(base_url + '/register')
        #enter valid email
        self.type("#email", "test_frontend@test.com")
        #enter valid Name
        self.type("#name", "test_frontend")
        #enter matching passwords
        self.type("#password", "valid_Pass")
        self.type("#password2", "valid_Pass")
        #Display proper error message 
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("User Already exists", "#message")


        


        

        
        