import urllib.request
import json
from urllib.parse import urlparse

#####
# This is the URLLIB tutorial
#####
title = "URLLIB Tutorial"
print(title)


# Parsing
print("\nParsing\n")

o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
print(dir(o))
print(o.hostname)
print(o.port)
print(o)

# Fetch HTML
print("\nParsing\n")

x = urllib.request.urlopen('https://www.google.com/')
print(x.read())

# Basic with header
print("\nBasic with Header\n")
header={'CustomHeader': 'CustomValue'}

# create the request
req = urllib.request.Request(url='http://www.yahoo.com/', headers=header, method='GET')
res = urllib.request.urlopen(req, timeout=5)

print(res.status)
print(res.reason)


# POST
print("\nPOST\n")


header={'CustomHeader': 'CustomValue'}

# create the request

# Payload
# Data dict
data = { 'test1': 10, 'test2': 20 }

# Dict to Json
# Difference is { "test":10, "test2":20 }
data = json.dumps(data)

# Convert to String
data = str(data)

# Convert string to byte
data = data.encode('utf-8')

# if data != None, will be POST
req = urllib.request.Request(url='http://www.yahoo.com/', headers=header, method='POST', data=data)
res = urllib.request.urlopen(req, timeout=5)


print("Status:{}, Reason:{}".format(res.status,res.reason))

res_body = res.read()
print("res body: {}".format(res_body.decode("utf-8")))
# data = urllib.urlencode({'s': 'Post variable'})
# h = httplib.HTTPConnection('https://server:80/')
# headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# h.request('POST', 'webpage.php', data, headers)
# r = h.getresponse()
# print(r.read())