import re

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and
# the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_1479360.txt (There are 88 values and the sum ends with 693)


fname = input("Enter file name: ")

try:
    fhandl = open(fname)

except:
    print("File cannot be opened:", fname)
    exit()

sub = 0
values = 0

for line in fhandl:
    stuff = re.findall("[0-9]+", line)
    if len(stuff) < 1 :
        continue

    for numbers in stuff:
        sub += int(numbers)
        values += 1

print(f"There are {values} Values with a sum = {sub}")

print( sum( [int(num) for num in re.findall('[0-9]+', open('regex_sum_42.txt').read())] ) )




# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1479362.html (Sum ends with 34)


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')

sub = 0
count = 0
for tag in tags:
    # Look at the parts of a tag
    numbers = re.findall("[0-9]+", str(tag))
    if len(numbers) < 1 : continue

    for number in numbers:
        sub += int(number)
        count += 1

print(f"Count: {count} \nSum: {sub}")




# We provide two files for this assignment.
# One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Elli.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: P



import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL -')
repeat = int(input('Enter number of repeatations: '))
position = int(input('Enter the link position: '))

#to repeat desired times
for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count +1

        #stopping at desired position
        if count>position:
            break
        url = tag.get('href', None)
        name = tag.contents[0]

print(name)



# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1479364.xml (Sum ends with 33)



import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from urllib.request import urlopen


api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    url = input('Enter location: ')
    if len(url) < 1: break

    data = urllib.request.urlopen(url, context=ctx).read().decode()

    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)
    counts = tree.findall('.//count')

    print(f"Count: {len(counts)}")

    lst = []
    for item in counts:
        numbers = int(item.text)
        lst.append(numbers)
    print(f"Sum: {sum(lst)}")





# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1479365.json (Sum ends with 89)


import urllib.request, urllib.parse, urllib.error
import ssl
from urllib.request import urlopen
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    url = input('Enter location: ')
    if len(url) < 1: break

    data = urllib.request.urlopen(url, context=ctx).read().decode()

    print('Retrieved', url)
    print('Retrieved', len(data), 'characters')

    js = json.loads(data)
    # print(json.dumps(js, indent=1))
    lst = []
    count = 0
    for item in js["comments"]:
        # print(item["count"])
        numbers = item["count"]
        lst.append(numbers)
        count += 1
    print("Count:", count)
    print("Sum:", sum(lst))




# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
# and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.


import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = {}
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

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
        continue

    # print(json.dumps(js, indent=1), "\n") # to convert py obj "js" to json string
    # and "indent" for how spaces look like between json string

    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    place_id = js['results'][0]['place_id']
    print("Place ID:", place_id)



###################################################################################################################


import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])