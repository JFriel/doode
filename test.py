#import urllib
#urllib.urlretrieve("http://www.stvedas.co.uk/webcam-images/webimg0.jpg", "webimg0.jpg")

#import ghost
#from ghost import Ghost
#ghost = Ghost()
#ghost.open('http://www.st-andrews.ac.uk/~iam/eastsands-flash.html')
#ghost.capture_to('screen_shot.png')
#############################################################################

import urllib2
import bs4
import re
from bs4 import BeautifulSoup

page = urllib2.urlopen('http://www.stvedas.co.uk/webcam-images/').read()
soup = BeautifulSoup(page)
#soup = soup.find_all("div", {"class": "span6"})
#print soup
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
#    link = link["src"].split("src=")[-1]
#    <a href="/example/11/1"> 
#   <img src="http://example.net/example.jpg" alt="Example"/>
#</a>
#    
#    <div class='span6'><img src='webimg0.jpg' alt='webcam photo' width='400px'><p>February 13 2016 13:01:36.</p></div>
# ############################################################################   
#    import ghost

#g = ghost.Ghost(4)
#with g.start() as session:
#    page, extra_resources = session.open("http://www.st-andrews.ac.uk/~iam/eastsands-flash.html")
#    if page.http_status == 200:
#        print("Good!")
#        page.capture('screen_shot.png')