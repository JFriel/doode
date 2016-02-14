import numpy as np
import matplotlib.pyplot as pt
import re
import time

def make_plot():

	with open("data.txt", "a") as f :

		while f.readline() is not none
			try:
				tokens = f.readline().split()
			except: 
				print 'error'
					
			stamp = tokens[0].replace("_", " ").replace("."," ").split()

			seconds = stamp[3]*1200 + stamp[4]*60 + stamp[5]




			if stamp[1] is 13:

				t.append(tokens[3])
				s.append(seconds)



			elif stamp[1] is 14:	

			
			
		
		
		
		plt_13.plot(t, s)
		#plt_14.plot(t, s)


		plt13.xlabel('seconds')
		plt13.ylabel('wavelength')
		plt13.title("live stream data 13th Feb")
		plt13.grid(True)
		plt13.savefig("live stream data 13th Feb")

		#plt14.xlabel('seconds')
		#plt14.ylabel('savelength')
		#plt14.title("live stream data 14th Feb")
		#plt14.grid(True)
		#plt14.savefig("live stream data 14th Feb")
	#plt.show()