#####
# This is the Lists, Tuple, Range tutorial
#####
title = "Lists, Tuple, Range Tutorial"
print(title)

# Lists
myList = [1, 2, "Apple"]
print(myList)
numList = [1, 2, 123, 3.45]
# List function
print(2 in myList)  # => True, if entry is in the list
print(2 not in myList)  # => False, if entry is NOT in the list

print(myList[2])  # => Apple, entry at said pos
print(len(myList))  # => 3
print(min(numList))  # => 1, must be all numeric
print(max(numList))  # => 123,  must be all numeric
print(numList.count(2))  # => 1, number of entries

mutableList = []
mutableList.append(2)  # add the entry to end
print(mutableList)
mutableList[0] = 'two'  # replace the content at said position
print(mutableList)

mutableList.extend([2, 3])  # add the new list to the end of the list
print(mutableList)
mutableList.insert(2, 4)  # add the object to position 2
print(mutableList)

mutableList.remove(4)  # remove object
print(mutableList)

print(mutableList.pop(0))  # 'two' the object at 0 position is removed and returned
print(mutableList)
mutableList.reverse()
print(mutableList)
mutableList.extend([100, 234])

print(mutableList)

mutableList.sort()
print(mutableList)  # new sorted list

mutableList.copy()  # shallow copy
mutableList.clear()
print(mutableList)  # empty

# Tuple (immutable)
# use parentheses
myTuple = ('a', 'b', 'c')  # ('a', 'b', 'c')
print(myTuple)

# Range (immutable)
# class range(stop)
# class range(start, stop[, step])
print(list(range(5)))  # [0, 1, 2, 3, 4],  0 to 4
print(list(range(0, 5)))  # [0, 1, 2, 3, 4],  0 to 4
print(list(range(0, 30, 5)))  # [0, 5, 10, 15, 20, 25],  0 to 30 step of 5

print(list(range(0, -10, -1)))  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9],  0 to -10 step of -1

