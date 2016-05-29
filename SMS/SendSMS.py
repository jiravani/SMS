from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "AC89d402c514180648e06a11e535dda1b7"
AUTH_TOKEN = "342109ebe78d778e3b97ffec61fd6cce"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
m = "Heetin"
p = "8016868394"
message = client.messages.create(
    body=m,  # Message body, if any
    to="+1"+p,
    from_="+18016959361",
 )
print(message.sid)