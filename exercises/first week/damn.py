from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC3310307d153ec0ce9bbb3fdc8ac08fbf'
auth_token = '7301cb1a39e5fa545b73cae656cbeac3'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+16822434068',
         to='+972543263304'
     )

print('success')
print(message.sid)