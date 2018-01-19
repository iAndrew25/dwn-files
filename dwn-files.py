import urllib;
import urlparse
import mechanize
import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="URL of the page you want to download files.")
parser.add_argument("-f", "--file", required=True, help="File extension to download.")
args = parser.parse_args()

print "        _                   __ _ _            "
print "       | |                 / _(_) |           "
print "     __| |_      ___ __   | |_ _| | ___  ___  "
print "    / _` \ \ /\ / / '_ \  |  _| | |/ _ \/ __| "
print "   | (_| |\ V  V /| | | | | | | | |  __/\__ \ "
print "    \__,_| \_/\_/ |_| |_| |_| |_|_|\___||___/ "
print "                                              "

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

visited = []
count = 0
extension = '.' + args.file

if not os.path.exists(extension):
	os.mkdir(extension)

br.open(args.url)

for link in br.links():
	newurl = urlparse.urljoin(link.base_url, link.url)
	if newurl.endswith(extension) and newurl not in visited:
		count += 1
		visited.append(newurl)
		f = open(extension + '/' + str(count) + '_' + link.text, 'wb')
		f.write(urllib.urlopen(newurl).read())
		f.close()
		sys.stdout.writelines ("Files downloaded: " + str(count) + "\n")
		sys.stdout.flush()

print "DONE!"