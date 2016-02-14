from image import *
import time
from scrape_eastsands import *
from scrape_coldingham import *

while (True):

	#scrape_eastsands()
	print "scraped eastsands"
	#scrape_coldingham()
	print "scraped coldingham"
	check_file()
	print "data collected for coldingham"

	time.sleep(2400)
