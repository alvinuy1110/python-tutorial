#####
# This is the OOP tutorial
#####
title = "OOP Tutorial"
print(title)

# Basic class
print("\nClass Attributes\n")


# Naming  Type  Meaning
# name   public  These attributes can be freely used indise or outside of a class definition.
# _name  Protected   attributes should not be used outside of the class definition, unless inside of a subclass
# __name private attribute is accessible and invisible. It's neither possible to rea nor write to those attribute except inside the class definition itself

# class declaration
class A():
    # constructor method
    def __init__(self):
        print("classA initialized")
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

    def get_private(self):
        return self.__priv


# Main stuff
a=A()   # constructor
print(a.pub)
a.pub = a.pub + " new value"
print(a.pub)

print(a._prot)

# a.__priv   # will throw error, not accessible
print(a.get_private())  # get via method


