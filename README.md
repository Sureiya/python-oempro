python-oempro
=============

A python 3.x client for oempro.

Very feature incomplete. Please feel free to work and add what you need.

You can clone and use directly, or install with pip.

pip-3.2 install -e git+git://github.com/Sureiya/python-oempro.git#egg=python-oempro

Example:

from oempro import api

client = api.client("http://example.org/oempro/api.php", 'client-username', 'login-password')

subscribers = client.get_subscribers(1)

print(subscribers)

