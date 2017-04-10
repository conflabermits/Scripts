from twilio.rest import Client

# Your Account SID from https://www.twilio.com/console/account/settings
account_sid = "AXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from https://www.twilio.com/console/account/settings
auth_token  = "xxxxxxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1xxxxxxxxxx",
    from_="+1xxxxxxxxxx",
    body="Hello from Python!")

print(message.sid)
