import urllib2
import bs4
import re
from bs4 import BeautifulSoup

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

page = urllib2.urlopen('http://surfershotel.remotemanager.co.uk/app/be64afcea5b4e81d9c57e241589b45b3/gallery').read()
soup = BeautifulSoup(page)


for img in soup.find_all("div", {"class": "thumb"}):
	pattern = re.compile("title=\"(.*?)\"")
	m = pattern.search(str(img))
	stamp = str(m.group(1)).split()
	time = stamp[1].replace(":", " ").split()
	
	if(stamp[2] == 'pm'):
		hour = int(time[0]) + 12
	else:
		hour = int(time[0])		
	stamp[1] = time[0]+"_"+time[1]+"_"+time[2]
	
	date = stamp[0].replace("/", " ").split() 
	stamp[0] = str(months[int(date[1])-1])+'_'+date[0]+'_20'+date[2]  

	img = img.find("a")
	
	image = urllib2.urlopen('http://surfershotel.remotemanager.co.uk/app/be64afcea5b4e81d9c57e241589b45b3/gallery'+img['href']).read()
	soup_image = BeautifulSoup(image)

	with open("images_eastsands/"+stamp[0]+"_"+stamp[1]+".jpg", "wb") as f :
		image = soup_image.find("img")
		#if image["src"] != None:
		f.write(urllib2.urlopen("http://surfershotel.remotemanager.co.uk"+image['src']).read())