import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC22bf26fe3fb7f01734943b0a1789e72e']
auth_token = os.environ['e777d9c3c67ae6fac5f20d1a2a34e8f9']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Testing if this works ishaan",
                     from_='+18607173110',
                     to='+19259643840'
                 )

print(message.sid)
