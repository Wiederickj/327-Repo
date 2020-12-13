import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
#testing that 404 error page shows up for all unknown pages 
@pytest.mark.usefixtures('server')
class R8TestCase(BaseCase):
    def test_error_page_register(self):
        self.open(base_url + '/Register')
        self.assert_element("#welcome-header")
        self.assert_text("404 - Page Not Found!", "#welcome-header")
    
    
    def test_error_page_wallet(self):
        self.open(base_url + '/Wallet')
        self.assert_element("#welcome-header")
        self.assert_text("404 - Page Not Found!", "#welcome-header")

    
    def test_error_page_profile(self):
        self.open(base_url + '/Profile')
        self.assert_element("#welcome-header")
        self.assert_text("404 - Page Not Found!", "#welcome-header")

    def test_any_other_page(self):
        self.open(base_url + '/AnyOtherPage')
        self.assert_element("#welcome-header")
        self.assert_text("404 - Page Not Found!", "#welcome-header")
