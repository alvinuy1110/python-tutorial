import json
#####
# This is the FILE IO JSON tutorial
#####
title = "FILE IO JSON Tutorial"
print(title)

# Basic write
print("\nFile Write\n")

filename="test.json"

myMap = {"key1": "value1", "key2": "value2"}

print(json.dumps(myMap))    # output to console

f = open(filename, 'w')

json.dump(myMap, f)
f.close()
print(f.closed) # True if closed

# read the file
f = open(filename, 'r')
myObj = json.load(f)

print ("The json obj is {}".format(myObj))

f.close()
print(f.closed) # True if closed
