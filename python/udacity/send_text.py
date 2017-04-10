from twilio import rest

# Your Account SID from https://www.twilio.com/console/account/settings
account_sid = "AXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from https://www.twilio.com/console/account/settings
auth_token  = "xxxxxxxxxxxxxxxxxxxxxx"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+1xxxxxxxxx",
    from_="+1xxxxxxxxxx",
    body="ANOTHER Hello from Python!")

print(message.sid)
