# Devolver latitude, longitude e endereço a partir da localização

import urllib.request, urllib.parse, urllib.error
import json

service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    adress = input('Enter location: ')
    if len(adress) < 1: break

    url = service_url + urllib.parse.urlencode({'adress': adress})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== ERROR TO RETRIEV ===')
        print(data)
        continue

    lati = js["results"][0]["geometry"]["location"]["lat"]
    long = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lati, 'lng', long)
    print(js['results'][0]['formatted_adress'])