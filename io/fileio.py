#####
# This is the FILE IO tutorial
#####
title = "FILE IO Tutorial"
print(title)

# Basic write
print("\nFile Write\n")

filename="test.txt"

f = open(filename, 'w')

f.write("this is a text string\n")
f.write("this is the seoncd line\n")
f.write("this is the third line\n")
f.close()

# Basic read
print("\nFile Read\n")

# this will read the entire file in one shot and close automatically
# not really recommended for large files
with open(filename) as f:
    read_data = f.read()
    print(read_data)

print(f.closed) # True if closed
print("\nFile Read (Efficient)\n")
f = open(filename)
for line in f:
    print(line, end='')

print()
f.close()
print(f.closed) # True if closed

# Read using seek
print("\nFile Read (Seek-Tell)\n")
f = open(filename)
print(f.readline())
f.seek(0)   # go to start again
print(f.tell())
print(f.readline())
f.close()
print(f.closed)  # True if closed

