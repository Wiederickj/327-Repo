import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash



#Sample user

new_test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_Frontend0!')
)

@pytest.mark.usefixtures('server')
class R7TestCase(BaseCase):
    
    @patch('qa327.backend.get_user', return_value=new_test_user)
#Logout will invalid the current session and redirect to the login page. 
    def test_logout(self, *_):
    # open login page
        self.open(base_url + '/login')
    # fill in the correct email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
    # click enter button
        self.click('input[type="submit"]')
    # Click logout button
        self.open(base_url + '/logout')
    #test if the page loads correctly
        self.assert_element("#message")
        #self.assert_text("Please Login", "#message")

 #After logout, the user shouldn't be able to access restricted pages.   
    def test_other_pages(self):
        self.open(base_url + '/login')
        self.open(base_url)
        self.assert_element("#message")
        #self.assert_text("Please Login", "#message")
        