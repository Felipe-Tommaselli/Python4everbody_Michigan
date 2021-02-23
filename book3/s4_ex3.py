# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
i = 0
while i < 7:
    tags = soup('a')
    all_tags = list()

    for tag in tags:
        all_tags.append(tag.get('href', None))

    html = urllib.request.urlopen(all_tags[17], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    i += 1

# http://py4e-data.dr-chuck.net/known_by_Anayah.html
# http://py4e-data.dr-chuck.net/known_by_Emon.html

words = all_tags[17].split('.')
words2 = words[2].split('_')

print(words2[2])