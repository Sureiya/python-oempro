import random
import oempro
import re


class TestOEMProAPI():
	api_url = ''
	api_username = ''
	api_password = ''

	def __init__(self):
		self.api = oempro.API(api_url, api_username, api_password)

	def setup(self):
		return self.api.login()

	def test_login(self):
		session_id = self.api.login()
		assert (re.match('^[\w-]+$', session_id) is not None)

	def test_subscribers_get(self):
		result = self.api.get_subscribers(2)
		assert (result is not None)
