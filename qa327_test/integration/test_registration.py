# import pytest
# from seleniumbase import BaseCase

# from qa327_test.conftest import base_url


# # integration testing:

# @pytest.mark.usefixtures('server')
# class Registered(BaseCase):
# #Create a new user
#     def register(self):
#         self.open(base_url + '/register')
#         self.type("#email", "test_integration@test.com")
#         self.type("#name", "test0")
#         self.type("#password", "Test0!qwertyuiop")
#         self.type("#password2", "Test0!qwertyuiop")
#         self.click('input[type="submit"]')

# #Test the login and logout features
#     def test_register_login(self):
#         self.register()
#         self.login()
#         self.open(base_url)
#         self.assert_element("#welcome-header")     
# #Login and see if user can be signed in
#     def login(self):
#         self.open(base_url + '/login')
#         self.type("#email", "test_integration@test.com")
#         self.type("#password", "Test0!qwertyuiop")
#         self.click('input[type="submit"]')

   

        