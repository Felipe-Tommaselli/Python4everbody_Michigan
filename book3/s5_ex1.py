import urllib.request, urllib.error
import xml.etree.ElementTree as ET

url = input('url: ')
output = urllib.request.urlopen(url).read()
tree = ET.fromstring(output)

total = 0
for comments in tree.findall('comments'):
    for comment in comments.findall('comment'):
        total += int(comment.find('count').text)

print(total)