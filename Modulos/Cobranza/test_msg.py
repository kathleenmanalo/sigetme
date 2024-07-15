import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACb6310d58e39377385dd671b69a552e7d']
auth_token = os.environ['e46a8d257dfbf420bc6bd9f316f2a21a']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12562861849',
                     to='+573102323724'
                 )

print(message.sid)