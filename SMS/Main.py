from twilio.rest import TwilioRestClient
import argparse

global account_sid
global auth_token

account_sid = "AC89d402c514180648e06a11e535dda1b7"  # Your Account SID from www.twilio.com/console
auth_token = "342109ebe78d778e3b97ffec61fd6cce"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

parser = argparse.ArgumentParser(description="Send a Twilio SMS with a given message to a given recipient.")
parser.add_argument("-a", "--accountid", action='store_true',
                    help="Twilio account number")
parser.add_argument("-m", "--message",
                    help="Message to be sent")
parser.add_argument("-p", "--phonenumber", type=int,
                    help="Recipient phone number")
parser.add_argument("-v", "--variable",
                    help="Some persistent variable")
args = parser.parse_args()

if args.accountid:
    print("Twilio Account SID: " + account_sid)
    exit()
if (args.phonenumber and not args.message) or (not args.phonenumber and args.message):
    parser.error("A message and a phonenumber are required to send an SMS")
    exit()
if args.phonenumber and len(str(args.phonenumber)) != 10:
    parser.error("Phone number requires 10 digits")

if args.phonenumber and args.message:
    m = client.messages.create(body=args.message,
                           to="+1"+str(args.phonenumber),  # Replace with your phone number
                           from_="+18016959361")  # Replace with your Twilio number
    if m.sid:
        print("SMS sent successfully.")
        print(m.sid)
