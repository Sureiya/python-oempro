#!/usr/bin/env python2.7
from urllib import urlopen, urlencode
import json


class Client:
	session_id = None

	def __init__(self, api_url, username, password):
		self.api_url = api_url
		self.username = username
		self.password = password
		self.session_id = self.login()

	def request(self, data, session_id=None):
		if session_id is None:
			data.update({'ResponseFormat': 'JSON', 'SessionID': self.session_id})
		else:
			data.update({'ResponseFormat': 'JSON', 'SessionID': session_id})
		data_string = urlencode(data).encode('ascii')
		print(self.api_url, data_string)
		response = urlopen(self.api_url, data_string)
		response_json = response.read().decode('utf8')
		return json.loads(response_json)

	def login(self):
		data = {
			'Command': 'User.Login',
			'Username': self.username,
			'Password': self.password,
			'RememberMe': 'true',
			'DisableCaptcha': 'true',
		}
		login_instance = self.request(data, session_id='')
		if login_instance['Success'] is not True:
			raise LoginError(login_instance['ErrorCode'][0])
		return login_instance['SessionID']

	def get_subscribers(self, list_id, segment='Active', order_by='SubscriptionDate', order_direction="DESC", records=50, search_field='', search_keyword=''):
		data = {
			'Command': 'Subscribers.Get',
			'SubscriberListID': list_id,
			'OrderField': order_by,
			'OrderType': order_direction,
			'RecordsPerRequest': records,
			'SearchField': search_field,
			'SearchKeyword': search_keyword,
			'SubscriberSegment': segment,
		}
		subscribers = self.request(data)
		return subscribers

	def get_subscriber(self, list_id, email_address):
		data = {
			'Command': 'Subscriber.Get',
			'ListID': list_id,
			'EmailAddress': email_address
		}
		subscribers = self.request(data)
		return subscribers

	def subscribe(self, list_id, email_address, ip_address='', custom_fields=None):
		data = {
			'Command': 'Subscriber.Subscribe',
			'ListID': list_id,
			'EmailAddress': email_address,
			'IPAddress': ip_address,
		}
		if custom_fields:
			for key, data in custom_fields:
				data['CustomField{0}'.format((int)key)] = data
		response = self.request(data)
		return response

	def unsubscribe(self, list_id, email_address, ip_address='', campaign_id='', email_id=''):
		data = {
			'Command': 'Subscriber.Unsubscribe',
			'ListID': list_id,
			'EmailAddress': email_address,
			'CampaignID': campaign_id,
			'EmailID': email_id,
			'IPAddress': ip_address,
		}
		response = self.request(data)
		return response


class APIError(Exception):
	error_messages = {99998: 'Authentication Failure or Session Expired',
		99999: 'Not Enough Priveleges'}


class LoginError(APIError):
	error_messages = {
		1: 'Username missing',
		2: 'Password Missing',
		3: 'Invalid Login Info',
		4: 'Invalid image verification',
		5: 'Image verification failed',
	}

	def __init__(self, value):
		self.value = value
		self.error_messages.update(APIError.error_messages)

	def __str__(self):
		return repr(self.error_messages[self.value])
