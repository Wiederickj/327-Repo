import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

# Testing the whole system (frontend+backend)

@pytest.mark.usefixtures('server')
class buy_post(BaseCase):
#Create new user
    def register(self):
        self.open(base_url + '/register')
        self.type("#email", "test_integration@test.com")
        self.type("#name", "test0")
        self.type("#password", "Test0!qwertyuiop")
        self.type("#password2", "Test0!qwertyuiop")
        self.click('input[type="submit"]')
#Login with new user
    def login(self):
        self.open(base_url + '/login')
        self.type("#email", "test_integration@test.com")
        self.type("#password", "Test0!qwertyuiop")
        self.click('input[type="submit"]')
#Sell the ticket
    def sell_ticket(self):
        self.open(base_url + '/')
        self.type("#sell_name", "HockeyStick")
        self.type("#sell_quantity", "1")
        self.type("#sell_price", "150")
        self.type("#sell_exp_date", "2077\t11-15")
        self.click("#sell_submit")
#Logout
    def logout(self):
        self.open(base_url + '/logout')
#make a new account so you can purchase a ticket
    def register_new(self):
        self.open(base_url + '/register')
        self.type("#email", "test_integration2@test.com")
        self.type("#name", "test2")
        self.type("#password", "Test0!qwertyuiop")
        self.type("#password2", "Test0!qwertyuiop")
        self.click('input[type="submit"]')
#login with this new account
    def login_with_new(self):
        self.open(base_url + '/login')
        self.type("#email", "test_integration2@test.com")
        self.type("#password", "Test0!qwertyuiop")
        self.click('input[type="submit"]')
 #buy the ticket   
    def buy_ticket(self):
        self.open(base_url + '/')
        self.click("#ticket-HockeyStick-buy")
        self.click("#buy_submit")
#see if ticket works by buying it and running test
    def test_buy_ticket(self):
      self.register()
      self.login()
      self.sell_ticket()
      self.logout()
      self.register2()
      self.login2()
      self.buy_ticket()
      self.open(base_url + "/")
      self.assert_element_absent("#ticket-HockeyStick")