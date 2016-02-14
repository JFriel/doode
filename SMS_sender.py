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

# Parsing the user input into valid phone numbers. Valid format is as follows: "+447584429236". 
# Should be properly parsed from "07584429236" or "447584429236" or "+447584429236" everything else is invalid syntax
phone_number_array = []     
for line in open("web/static/edinburgh_numbers.txt", 'r'):
	if(line[0:2] == '44' and (line[12] == '\n' or line[12] == ' ')):
		array = '+' + line[0:12]
		phone_number_array.append(array)
	elif(line[0:3] == '+44' and (line[13] == '\n' or line[13] == ' ')):
		array = line[0:13]
		phone_number_array.append(array)
	elif(line[0:2] == '07' and (line[11] == '\n' or line[11] == ' ')):
		array = '+44' + line[1:11]
		phone_number_array.append(array)

print phone_number_array

def sendtext():

	# Find these values at https://twilio.com/user/account
	account_sid = "AC0035cee82225e4f04cf4a922e9412e55"
	auth_token = "dc537119815f8131bf6314416ffb196f"
	client = TwilioRestClient(account_sid, auth_token)

	for phoneNum in phone_number_array:
		# Twilio Number: +441133207976
		print phoneNum
		message = client.messages.create(to=str(phoneNum), from_="+441133207976", body="Surf's up brah!")


if __name__ == "__main__":
    sendtext();