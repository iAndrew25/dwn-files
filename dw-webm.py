import urllib;
import urlparse
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open("http://boards.4chan.org/wsg/thread/2062256")

for link in br.links():
	newurl = urlparse.urljoin(link.base_url, link.url)
	if newurl.endswith('.webm'):
		f = open(link.text + '.webm', 'wb')
		f.write(urllib.urlopen(newurl).read())
		f.close()