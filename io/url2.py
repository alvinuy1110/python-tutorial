import urllib.request
from urllib.parse import urlparse
import json

#####
# This is the URLLIB2 tutorial
#####
title = "URLLIB2 Tutorial"
print(title)


# https://docs.python.org/3/library/urllib.request.html#examples
# https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
res = urllib.request.urlopen('https://ip-ranges.amazonaws.com/ip-ranges.json')

print(dir(res))
print("Status:{}, Reason:{}".format(res.status,res.reason))
res_body = res.read()

# https://docs.python.org/3/library/json.html

print("res body: {}".format(res_body.decode("utf-8")))
j = json.loads(res_body.decode("utf-8"))

# parse strings: 'ip_prefix' and 'region'
# for i in range(len(j['prefixes'])):
#	print("{0}\t{1}".format(j['prefixes'][i]['ip_prefix'], j['prefixes'][i]['region']))
print(j)
for prefix in j['prefixes']:
    print("{0}\t{1}".format(prefix['ip_prefix'], prefix['region']))
