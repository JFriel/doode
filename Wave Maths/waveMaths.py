import math

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


	return "period: " + str(period) + ", frequency: " + str(frequency) + ", speed: " + str(speed)

def gnarometer(wavelength,period,frequency):
    return wavelength * (period*2) + (frequency*1.5)

# Test line with lines 3y = 4x + 7 and 5y = 3x + 6, should return 0.543.., freq 1.84, speed 69
print waveMaths([3,4,7], [5,3,6], 69)

