import urllib.request, urllib.parse, urllib.error
import json

serviceUrl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location')
url = serviceUrl + urllib.parse.urlencode({'address': address})

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), 'characters')

try:
	js = json.loads(data)
except:
	js = None

if not js or 'status' not in js or js['status'] != 'OK':
	print('==== Failure to Retrieve ====')
	print(data)

print(json.dumps(js, indent=4))

id = js['results'][0]['place_id']
print(id)

