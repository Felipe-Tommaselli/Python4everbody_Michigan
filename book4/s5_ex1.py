# 
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import ssl
import time, sys

api_key = False
#
#

if api_key is False:
    serviceurl = 'http://python-data.dr-chuck.net/geojson?'
else:
    serviceurl = 'https://py4e-data.dr-chuck.net/geojson'

# 
#

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (adress TEXT, geodata TEXT)''')

#
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 200:
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE adress= ?", 
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print('Found in database', address)
        continue
    except:
        pass

    parms = dict()
    parms["query"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode('utf8')
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count += 1

    try:
        js = json.loads(data)
    except:
        print(data)
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print('=== FAILURE TO RETRIEVE ===')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (adress, geodata)
                VALUES (?, ?)''', (memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()
    if count % 10 == 0:
        print('Pausing for a bit')
        time.sleep(5)

    print('END')