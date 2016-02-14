import math
from twilio.rest import TwilioRestClient
import time
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



def waveMaths(eqArray1, eqArray2, speed):
	# Takes in array defining the line equations and speed, returns array with wavelength, speed, frequency, period
	timesY1 = eqArray1[0]
	timesX1 = eqArray1[1]
	constant1 = eqArray1[2]

	timesY2 = eqArray2[0]
	timesX2 = eqArray2[1]
	constant2 = eqArray2[2]

	# Solving equation 1 for y when x = 0
	yZero1 = (constant1/timesY1)

	# Solving equation 2 for y when x = 0
	yZero2 = (constant2/timesY2)

	# taking distance between wave points when x = 0
	zeroDist = math.sqrt((yZero1 - yZero2)**2)

	# Solving equation 1 for when x = 100
	yHundred1 = (((100 * timesX1) + constant1)/ timesY1)

	# Solving equation 2 for y when x = 100
	yHundred2 = (((100 * timesX2) + constant2)/ timesY2)

	# taking distance between wave points when x = 100
	hundredDist = math.sqrt((yHundred1 - yHundred2)**2)

	# taking average distance between the two lines between x =0 and x = 10
	avgDist = ((hundredDist + zeroDist)/2)

	# Finds period and frequency of waves and returns them along with speed

	frequency = speed/avgDist
	period = 1/frequency
        gnarly = gnarometer(wavelength,period,frequency)

        return gnarly
	#return "period: " + str(period) + ", frequency: " + str(frequency) + ", speed: " + str(speed)

def gnarometer(wavelength,period,frequency):
    return wavelength * (period*2) + (frequency*1.5)

def sendtext():

	# Find these values at https://twilio.com/user/account
	account_sid = "AC0035cee82225e4f04cf4a922e9412e55"
	auth_token = "dc537119815f8131bf6314416ffb196f"
	client = TwilioRestClient(account_sid, auth_token)

	for phoneNum in phone_number_array:
		# Twilio Number: +441133207976
		print phoneNum
		message = client.messages.create(to=str(phoneNum), from_="+441133207976", body="Surf's up brah!")

while True:
    gn = waveMaths(eqArray1,eqArray2,speed)
    if (gn >= 50):
        sendtext()
        time.sleep(10800)
    else:
        time.sleep(1200)






# Test line with lines 3y = 4x + 7 and 5y = 3x + 6, should return 0.543.., freq 1.84, speed 69
print waveMaths([3,4,7], [5,3,6], 69)

