# 

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore ssl certificate errors (não precisa se preocupara com isso)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verofy_mode = ssl.CERT_NONE

url = input('Enter: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
tags = soup('a') # essa é a tag que procuramos o '<a' do html
for tag in tags:
    print(tag.get('href', None))

# pode tentar o http://www.dr-chuck.com/page1.htm ou o http://www.dr-chuck.com
# o segundo tem mais tags nele

