import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend homepage.
"""

#sample user
new_test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_Frontend0!'),
    balance=100
)

#sample ticket 1
new_test_ticket_1 = Ticket(
    owner = 'test_frontend1@test.com',
    name='test_frontend1',
    quantity = 10,
    price = 10,
    date = '20210101'
)

#sample ticket 2
new_test_ticket_2 = Ticket(
    owner = 'test_frontend2@test.com',
    name='test_frontend2',
    quantity = 15,
    price = 15,
    date = '20210202'
)

#testing frontend user profile page
class UserProfilePageTestFrontEnd(BaseCase):
    
    #test R3.1
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_logged_out(self, *_):

        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
        
        #login page opens
        self.open(base_url + '/login')
        
    #test R3.2
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_hi_header(self, *_):
        
        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
        
        #login page opens
        self.open(base_url + '/login')
        
        #enter email and password of test_user into #email and #password elements
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        
        # click login button
        self.click('input[type="submit"]')
        
        # open user profile page
        self.open(base_url)
        
        #validate  welcome-header element exists and outputs correct phrase
        self.assert_element("#welcome-header")
        self.assert_text("Hi test_frontend", "#welcome-header")
        
    #test R3.3
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_user_balance(self, *_):
        
        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
        
        #login page opens
        self.open(base_url + '/login')
        
        #enter email and password of test_user into #email and #password elements
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        
        # click login button
        self.click('input[type="submit"]')
        
        # open user profile page
        self.open(base_url)
        
        #validate test_user balance is shown on page
        self.assert_element("#balance")
        self.assert_text("Your balance is $100", "#balance")
    """   
    #test R3.4
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_logout_link(self, *_):
        
        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
        
        #login page opens
        self.open(base_url + '/login')
        
        #enter email and password of test_user into #email and #password elements
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        
        # click login button
        self.click('input[type="submit"]')
        
        # open user profile page
        self.open(base_url)
        
        #validate logout link exists
        self.assert_element("#/logout")
        self.assert_text("logout", "#/logout")
     """"""   
    #test R3.5
    @patch('qa327.backend.get_user', return_value=new_test_user)
    @patch('qa327.backend.get_ticket', return_value=new_test_ticket_1)
    def test_available_tickets(self, *_):
        
        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
        
        #login page opens
        self.open(base_url + '/login')
        
        #enter email and password of test_user into #email and #password elements
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        
        # click login button
        self.click('input[type="submit"]')
        
        # open user profile page
        self.open(base_url)
        
        #validate all available tickets are shown
        self.assert_element("#tickets div h4")
        self.assert_text("test_frontend1 10", "#tickets div h4")
    """    
    #test R3.6
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_sell_form(self, *_):
        
        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
        
        #login page opens
        self.open(base_url + '/login')
        
        #enter email and password of test_user into #email and #password elements
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        
        # click login button
        self.click('input[type="submit"]')
        
        # open user profile page
        self.open(base_url)
        
        #validate sell form exists
        self.assert_element("#sell-header")
        self.assert_text("Sell a Ticket!", "#sell-header")
        
        #validate sell form includes #name element with correct attached phrase
        self.assert_element("#name")
        self.assert_text("Name", "#name")
        
        #validate sell form includes #quantity element with correct attached phrase
        self.assert_element("#quantity")
        self.assert_text("Quantity", "#quantity")
        
        #validate sell form includes price element with correct attached phrase
        self.assert_element("#price")
        self.assert_text("Price", "#price")
        
        #validate sell form includes date element with correct attached phrase
        self.assert_element("#date")
        self.assert_text("Expiration Date", "#date")
        
    #test R3.7
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_sell_form(self, *_):
        
        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
        
        #login page opens
        self.open(base_url + '/login')
        
        #enter email and password of test_user into #email and #password elements
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        
        # click login button
        self.click('input[type="submit"]')
        
        # open user profile page
        self.open(base_url)
        
        #validate buy form exists
        self.assert_element("#buy-header")
        self.assert_text("Buy a Ticket!", "#buy-header")
        
        #validate buy form includes #name element with correct attached phrase
        self.assert_element("#name")
        self.assert_text("Name", "#name")
        
        #validate buy form includes #quantity element with correct attached phrase
        self.assert_element("#quantity")
        self.assert_text("Quantity", "#quantity")
        
    #test R3.7
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_sell_form(self, *_):
        
        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
        
        #login page opens
        self.open(base_url + '/login')
        
        #enter email and password of test_user into #email and #password elements
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        
        # click login button
        self.click('input[type="submit"]')
        
        # open user profile page
        self.open(base_url)
        
        #validate update form exists
        self.assert_element("#update-header")
        self.assert_text("Update a Ticket!", "#update-header")
        
        #validate update form includes #name element with correct attached phrase
        self.assert_element("#name")
        self.assert_text("Name", "#name")
        
        #validate update form includes #quantity element with correct attached phrase
        self.assert_element("#quantity")
        self.assert_text("Quantity", "#quantity")
        
        #validate update form includes price element with correct attached phrase
        self.assert_element("#price")
        self.assert_text("Price", "#price")
        
        #validate update form includes date element with correct attached phrase
        self.assert_element("#date")
        self.assert_text("Expiration Date", "#date")
        
    #test R3.8
      
    #test R3.9  
    @patch('qa327.backend.get_user', return_value=new_test_user)
    @patch('qa327.backend.get_ticket', return_value=new_test_ticket_1)
    def test_sell_form(self, *_):
        
        # open /logout to invalidate any current logged in sessions
        self.open(base_url + '/logout')
        
        #login page opens
        self.open(base_url + '/login')
        
        #enter email and password of test_user into #email and #password elements
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        
        #click login button
        self.click('input[type="submit"]')
        
        #open user profile page
        self.open(base_url)
        
        #enter ticket name into #sell element
        self.type("#name", "test_frontend1")
        
        #enter quantity into #quantity element