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

test_tickets = [
    {'name': 't1', 'owner': 'bob', 'price': '100', 'quantity': '11', 'date': '20210101'}
]

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
        
        #click logout
        self.open(base_url + '/logout')

        #login page opens
        self.open(base_url + '/login')
      
    #test R3.5
    @patch('qa327.backend.get_user', return_value=new_test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
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
        self.assert_text("t1 100 11 20210101", "#tickets div h4")
        
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
              
        #enter ticket name into #sell_name element
        self.type("#sell_name", "test_frontend1")
        
        #enter quantity into #sell_quantity element
        self.type("#sell_quantity", 10)
        
        #enter price into #sell_price element
        self.type("#sell_price", 10)
        
        #enter expiration date into #sell_date element
        self.type("#sell_date", "20210101")
        
    #test R3.7
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_buy_form(self, *_):
        
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
        
        #enter ticket name into #buy_name element
        self.type("#buy_name", "test_frontend1")
        
        #enter quantity into #buy_quantity element
        self.type("#buy_quantity", 10)
                
    #test R3.8
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_update_form(self, *_):
        
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
        
        #enter ticket name into #update_name element
        self.type("#update_name", "test_frontend1")
        
        #enter quantity into #update_quantity element
        self.type("#update_quantity", 10)
        
        #enter price into #update_price element
        self.type("#update_price", 10)
        
        #enter expiration date into #update_date element
        self.type("#update_date", "20210101")
    
    #test R3.9  
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_sell_post(self, *_):
        
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
        
        #enter ticket name into #sell_name element
        self.type("#sell_name", "test_frontend1")
        
        #enter quantity into #sell_quantity element
        self.type("#sell_quantity", 10)
        
        #enter price into #sell_price element
        self.type("#sell_price", 10)
        
        #enter expiration date into #sell_date element
        self.type("#sell_date", "20210101")
        
        #click sell button
        self.click('input[value="sell"]')
        
    #test R3.10
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_buy_post(self, *_):
        
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
        
        #enter ticket name into #buy_name element
        self.type("#buy_name", "test_frontend1")
        
        #enter quantity into #buy_quantity element
        self.type("#buy_quantity", 10)
        
        #click buy button
        self.click('input[value="buy"]')
   
    #test R3.11
    @patch('qa327.backend.get_user', return_value=new_test_user)
    def test_update_post(self, *_):
        
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
        
        #enter ticket name into #update_name element
        self.type("#update_name", "test_frontend1")
        
        #enter quantity into #update_quantity element
        self.type("#update_quantity", 10)
        
        #enter price into #update_price element
        self.type("#update_price", 10)
        
        #enter expiration date into #update_date element
        self.type("#update_date", "20210101")
        
        #click update button
        self.click('input[value="update"]')    
   