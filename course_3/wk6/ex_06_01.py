import urllib.request
import json

url = input ("Enter location: ")
raw = urllib.request.urlopen(url).read().decode()
#print (raw)

content = json.loads(raw)
comments = content['comments']

sum = 0 
for comment in comments:
	#print (comment)
	sum += comment['count']

print(sum)
