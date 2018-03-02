#####
# This is the OOP tutorial
#####
title = "OOP Tutorial"
print(title)

# Basic class
print("\nBasic Class\n")


# class definition
class A():
    # constructor
    def __init__(self):
        print("classA initialized")

    # constructor
    def __init__(self, name=None):
        print("classA initialized")
        self.name=name

    def get_name(self):
        return self.name;

    def set_name(self, name):
        self.name = name;
        pass


# Main stuff
a = A()  # constructor
a.name="classA"
print(a.get_name()) # method call

# unknown property
# attr = a.prop1  # will throw an Error
attr = getattr(a,'prop1', 'defaultValue')   # safe retrieval and return defaultValue if not available
print(attr)

a.set_name("newClass")  # method invocation
print(a.get_name())

# constructor 2
a2=A("A2")
print(a2.get_name())

# call destructor
del a
del a2
