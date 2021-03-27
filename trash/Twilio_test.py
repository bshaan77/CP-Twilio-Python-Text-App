# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = os.environ['AC22bf26fe3fb7f01734943b0a1789e72e']
auth_token = os.environ['87cb3b9f88c30085dfd34fb6f916801b']

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+19259643840",
    from_="+18607173110",
    body="Hello there!")
