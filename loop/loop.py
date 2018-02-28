#####
# This is the Looping tutorial
#####
title = "Looping Tutorial"
print(title)

# Looping
print("\n\nLooping\n\n")
myMap = {"key1": "value1", "key2": 1234}
print(myMap)

# print the entries
print("\nKey-Value\n")
for (k, v) in myMap.items():
    print(k, v)

# loop with the index
print("\nIndex-Value\n")
for (i, v) in enumerate(myMap):
    print(i, v)

# loop 2 lists
print("\nZip example\n")
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# while if loop
print("\nWhile loop\n")
x = 0
while (True):
    if (x >= 5):
        break
    elif (x > 2):
        print("{0} is greater than 2".format(x))
        x = x + 1
    else:
        print(x)
        x = x + 1
