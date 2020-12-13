import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

# Testing the whole system (frontend+backend).

@pytest.mark.usefixtures('server')
class SellTicket(BaseCase):

    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "test_integration@test.com")
        self.type("#name", "test0")
        self.type("#password", "Test0!qwertyuiop")
        self.type("#password2", "Test0!qwertyuiop")
        self.click('input[type="submit"]')

    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "test_integration@test.com")
        self.type("#password", "Test0!qwertyuiop")
        self.click('input[type="submit"]')

    def sell_ticket(self):
        """ Add a ticket to be sold """
        self.open(base_url + '/')
        self.type("#sell_name", "Avengers")
        self.type("#sell_quantity", "3")
        self.type("#sell_price", "35")
        self.type("#sell_exp_date", "2022\t12-20")
        self.click("#sell_submit")

    def test_sell_ticket(self):
      """ This test checks the implemented sell 
      ticket feature """
      self.register()
      self.login()
      self.sell_ticket()
      self.open(base_url + "/")
      self.assert_element("#ticket-Avengers")
      self.assert_text("Avengers", "#ticket-Avengers-name")
      self.assert_text("3", "#ticket-Avengers-quantity")
      self.assert_text("35", "#ticket-Avengers-price")
      self.assert_text("2022-12-20", "#ticket-Avengers-date")