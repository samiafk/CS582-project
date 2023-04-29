
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Sends a text message to the 'to' number.
def sms(message):
    # Twilio Trial Credentials. If you want to try this with your own phone #
    # you have to create a trial account with Twilio, and replace the
    # account_ssid, auth_token, and 'from' number with the ones provided to you.
    # because the trial account only lets you send texts to your number.
    account_sid = 'ACb13e96f117302b4977bbc691bc13e753'
    auth_token = '699035538b9d24267438ea64e0fe9675'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=message,
                         from_='+18557432972',
                         to='+16192618153'
                     )

    message.sid


# Sends a string as an argument.
sms_message = 'This is a test message'
sms(sms_message)
