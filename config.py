from os import environ

token = environ.get("TOKEN")
assert token is not None
