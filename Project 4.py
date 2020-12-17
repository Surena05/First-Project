from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC23db03de205e24ddad6ceebd1fe60ab7"
# Your Auth Token from twilio.com/console
auth_token  = "1c9acf6e31514c153632bdf424982c1b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14164600803", 
    from_="+14155238886",
    body="Hello from Python!")

print(message.sid)
