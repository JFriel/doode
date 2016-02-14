import cv2
import numpy as np
import math
from scipy import cluster
import scipy
import heapq
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

class image():

	def __init__(self, name):
		
		self.look_image(name)

	def paralax_correction(self, measured_interval, cam_height, cam_distance):
		distance_to_measurement = math.sqrt(cam_height*cam_height+cam_distance*cam_distance)
		return measured_interval * distance_to_measurement * distance_to_measurement / (distance_to_measurement*cam_height - cam_distance*measured_interval)	

	def look_image(self, name):
		img_original = cv2.imread('test_waves/'+str(name)+'.jpg')
		cv2.imshow("frame2",img_original)
		img = img_original
		imgThresh = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
				#imgThreshLow = cv2.inRange(gray,(140, 0, 0),(170, 255, 255))
				#imgThreshHigh = cv2.inRange(gray,(0, 0, 0),(0, 200, 255))

				#imgThresh = cv2.add(imgThreshLow, imgThreshHigh)
				#
				#imgThresh = cv2.add(imgThreshLow, imgThreshHigh)

				#imgThresh = cv2.GaussianBlur(imgThresh, (3, 3), 2)                # blur

				#imgThresh = cv2.dilate(imgThresh, np.ones((5,5),np.uint8))        # close image (dilate, then erode)
		imgThresh = cv2.erode(imgThresh, np.ones((5,5),np.uint8))         # closing "closes" (i.e. fills in) foreground gaps

		points = np.zeros((70,1))

		thresh_num = 0
		while thresh_num < 70 :
		#print thresh_num
			edges = cv2.Canny(imgThresh, 40, thresh_num)
			lines = cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1);
			for line in lines[0]:
				pt1 = (-100000,line[1])
				pt2 = (100000,line[3])
				cv2.line(img, pt1, pt2, (0,0,255), 3)
				points[thresh_num] = line[1]	


			thresh_num = thresh_num + 1


		centroid, label = scipy.cluster.vq.kmeans2(points,12)
				#centroid, label = cophenet(points, pdist(points))

		#print centroid
		#print label
		tally = [0]*12	

		for x in label:
			tally[x]= tally[x] + 1
		#print tally
		i=0
		for point in centroid:
					#print int(point)
			if tally[i] is not 0 and point <= 550:
				cv2.circle(img, (0,int(point)),6, (0, 255, 0), 3)	
			i = i + 1

			if point > 550:
				centroid = np.delete(centroid, i)


		largest = heapq.nlargest(3,centroid)

		metre_per_pixel = 0.2

		water_line_reference = largest[0]
		break_length_paralax = (largest[0] - largest[1])*metre_per_pixel
		wave_length_paralax = (largest[1] - largest[2])*metre_per_pixel

		cv2.imshow("frame1",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cam_height = 26
        cam_distance = 220

        self.break_length = self.paralax_correction(self.break_length_paralax, cam_height, cam_distance)
        self.wave_length = self.paralax_correction(self.wave_length_paralax, cam_height, cam_distance + self.break_length)

		

	