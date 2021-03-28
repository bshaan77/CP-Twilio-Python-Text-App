import os
from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
#client = Client(account_sid, auth_token)

#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

my_msg = "Hey"
message = client.messages.create(to=my_cell, from_=my_twilio,body=my_msg)

def startSMS (name):
    my_msg = "Hey" + name + ", your workout will be starting soon"
    message = client.messages.create(to=my_cell, from_=my_twilio,body=my_msg)

def bookSMS (name):
    my_msg = "Hey" + name + ", your gym has been booked: *** For Dev Purposes we can send the google maps link here"
    message = client.messages.create(to=my_cell, from_=my_twilio,body=my_msg)

def endSMS (name):
    my_msg = "Hey" + name + ", your workout has ended: *** For Dev purposes we can send them a link to their data on the website. \n Schedule another session here: ***link"
    message = client.messages.create(to=my_cell, from_=my_twilio,body=my_msg)
    
