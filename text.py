from twilio.rest import Client
from codes import *

account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

# Initialize codes object
codes = Codes()

def send_text():
    status = codes.check_status()
    # Check if there are new codes or not
    if status is True:
        text = 'New codes have arrived! ' + str(codes.return_codes())
    else:
        text = 'No new codes. Here are the old ones: ' + str(codes.return_codes())
    message = client.messages.create (
        from_='',
        body =text,
        to=''
    )
    message.sid()
