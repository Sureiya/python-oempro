python-oempro
=============

A python 3.x client for oempro.

Very feature incomplete. Please feel free to work and add what you need.

You can clone and use directly, or install with pip.

(Make sure you are running python 3 pip by using pip --version)

```bash
pip install -e git+git://github.com/Sureiya/python-oempro.git#egg=python-oempro
```

Example:
========
```python
from oempro import api

client = api.client("http://example.org/oempro/api.php", 'client-username', 'login-password')

subscribers = client.get_subscribers(1)

print(subscribers)
```

Testing:
========

I haven't put much work in the tests, but you can get them running by installing nose, and adding your API credentials to tests.py

