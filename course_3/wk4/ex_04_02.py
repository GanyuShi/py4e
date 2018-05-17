from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ('Enter URL: ')
count = int(input ('Enter count: '))
position = int(input ('Enter position: '))

for i in range(count):
	html = urlopen (url, context = ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	url = tags[position-1].get('href', None)
	print("position", position, url )

print("final url:" , url)
name = re.findall("known_by_(.*).html", url)
print(name[0])
