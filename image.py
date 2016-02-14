import cv2
import numpy as np
import math
from scipy import cluster
import scipy
import heapq
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
import os
import imghdr





def check_file():

     
    path = 'images_coldingham/'
    listing = os.listdir(path)
    for infile in listing:
        print infile
        with open("data.txt", "wb") as f :
        	#if(imghdr.what(infile) == 'jpg'):
        	f.write(look_image(infile))
		


def look_image(name):
	print name
	img = cv2.imread('images_coldingham/'+name)
	imgThresh = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	imgThresh = cv2.erode(imgThresh, np.ones((5,5),np.uint8))         

	points = np.zeros((70,1))

	thresh_num = 0
	while thresh_num < 70 :
		#print thresh_num
		edges = cv2.Canny(imgThresh, 40, thresh_num)
		lines = cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1);
		for line in lines[0]:
			pt1 = (-100000,line[1])
			pt2 = (100000,line[3])
			#cv2.line(img, pt1, pt2, (0,0,255), 3)
			points[thresh_num] = line[1]	


		thresh_num = thresh_num + 1


	centroid, label = scipy.cluster.vq.kmeans2(points,20)
				

	tally = [0]*20	

	for x in label:
		tally[x]= tally[x] + 1
	#print tally
	i=0
	for point in centroid:
				#print int(point)
		if tally[i] is not 0 and point <= 550:
			pt1 = (-100000,int(point))
			pt2 = (100000,int(point))
			cv2.line(img, pt1, pt2, (19,201,253), 3)
		
		if point > 550:
			centroid = np.delete(centroid, i)
		i = i + 1
		
	
	largest = heapq.nlargest(3,centroid)
	
	water_line_reference = largest[0]
	break_length_paralax = (largest[0] - largest[1])
	wave_length_paralax = (largest[1] - largest[2])

	cam_height = 26
	cam_distance = 220

	return name+"	"+str(water_line_reference)+"	"+str(break_length_paralax)+"	"+str(wave_length_paralax)

	#cv2.imshow("frame",img)	
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

		
        
	