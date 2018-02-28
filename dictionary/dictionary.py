#####
# This is the Dictionary tutorial
#####
title = "Dictionary Tutorial"
print(title)

# Dictionary
# just like a JSON object
# not sorted
myMap = {"key1": "value1", "key2": 1234}
print(myMap)

myMap['key3'] = "someVa3"  # add the new entry
print(myMap)

del myMap['key3']  # delete entry
print(myMap)
# functions
print(list(myMap.keys()))  # get the keys

print(sorted(myMap.keys()))  # get the sorted keys

print(list(myMap.items()))  # items key-value pair
print(myMap.get('key1'))  # just get the value
print(myMap.get('key1222', 'blah'))  # just get the value, not present return the default value

print(myMap.pop('key1'))  # pop the said key if exists, return the value
print(myMap)

print(list(myMap.values()))  # list the values

myMap.clear()  # to empty

