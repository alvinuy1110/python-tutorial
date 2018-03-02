import os
from sys import platform

#####
# This is the Standard Library: OS tutorial
#####
title = "Standard Library: OS Tutorial"
print(title)

# OS
print(dir(os))
# print(help(os))

print("Platform: {}".format(platform))

if platform == "linux" or platform == "linux2":
    print(os.uname())
    print("Curr directory: {}".format(os.getcwd()))
    print("Curr userId: {}".format(os.getuid()))
    print("Environment variables: {}".format(os.environ))
    print(os.getenv("PATH"))
elif platform == "win32":
    print(os.name)
    print("Curr directory: {}".format(os.getcwd()))
    # print("Curr userId: {}".format(os.getuid()))
    print("Environment variables: {}".format(os.environ))
    print(os.getenv("PATH"))


# execute an os command
os.system('echo "hi there"')

print(os.cpu_count())

print("Random string: {}".format(os.urandom(2)))
