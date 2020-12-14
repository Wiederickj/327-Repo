import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

@pytest.mark.usefixtures('server')
class UpdateTicket(BaseCase):
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
#list a tickert for sale
    def sell_ticket(self):
        self.open(base_url + '/')
        self.type("#sell_name", "HockeyStick")
        self.type("#sell_quantity", "1")
        self.type("#sell_price", "150")
        self.type("#sell_exp_date", "2077\t11-15")
        self.click("#sell_submit")
#test if ticket price is updated
    def test_Update_ticket_for_sale(self):
      self.register()
      self.login()
      self.sell_ticket()
      self.open(base_url + "/")
      self.assert_element("#ticket-HockeyStick")
      self.assert_text("HockeyStick", "#ticket-HockeyStick-name")
      self.assert_text("1", "#ticket-HockeyStick-quantity")
      self.assert_text("150", "#ticket-HockeyStick-price")
      self.assert_text("2077-11-15", "#ticket-HockeyStick-date")