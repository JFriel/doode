import urllib2
import bs4
import re
from bs4 import BeautifulSoup

page = urllib2.urlopen('http://www.stvedas.co.uk/webcam-images/').read()
soup = BeautifulSoup(page)

counter = 0
for img in soup.find_all("div", {"class": "span6"}):
	stamp = img.find("p")
	pattern = re.compile("<p>(.*?).</p>")
	m = pattern.search(str(stamp))
	name = str(m.group(1)).split()
	name[3] = name[3].replace(":", "_")

	with open("images_coldingham/"+name[0]+"_"+name[1]+"_"+name[2]+"_"+name[3]+".jpg", "wb") as f :
		img = img.find("img")
		if img["src"] != None:
			f.write(urllib2.urlopen("http://www.stvedas.co.uk/webcam-images/"+img['src']).read())
	counter += 1