import schedule 
import time

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient


'''
****************************************************
***          Twilio account details:             ***
****************************************************
***  username/email: andrebododea@sbcglobal.net  ***
***        password: StirHack2016			     ***
****************************************************
'''


# Andre's Phone Number: +447584429236
# Dan's Phone number: +447935456467
phone_number_array = ["+447584429236","+447935456467"]

def sendtext():
	# Find these values at https://twilio.com/user/account
	account_sid = "AC0035cee82225e4f04cf4a922e9412e55"
	auth_token = "dc537119815f8131bf6314416ffb196f"
	client = TwilioRestClient(account_sid, auth_token)

	for phoneNum in phone_number_array:
		# Twilio Number: +441133207976
		print phoneNum
		message = client.messages.create(to=str(phoneNum), from_="+441133207976", body="Surf's up brah!")


# Sets scheduler to place a pending at 9:00 every day
schedule.every().day.at("9:00").do(sendtext)

# Loops forever, running the pending messages. 
while True:
	schedule.run_pending()
	time.sleep(1)