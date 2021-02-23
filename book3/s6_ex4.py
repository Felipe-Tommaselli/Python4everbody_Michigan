# dado um local achar o id do local

import urllib.request, urllib.parse, urllib.error
import json, ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = input('Location: ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = serviceurl + urllib.parse.urlencode({'key': api_key, 'address':address})

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    quit()

# print(json.dumps(js, indent=4)) 
# apenas formata o dicionario de lista js pra facilitar a leitura

print('place id', js['results'][0]['place_id'])
# meio redundante dizer [0] pois só ha um item, mas melhor garantir né

lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)