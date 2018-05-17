import urllib.request
import xml.etree.ElementTree as ET

url = input ('Enter location:')
xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)

comments = tree.findall('.//comment')
sum = 0
for comment in comments:
	count = comment.find('count').text
	sum += int(count)
print(sum)

