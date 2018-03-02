#####
# This is the OOP Inheritance tutorial
#####
title = "OOP Inheritance Tutorial"
print(title)

# Basic class
print("\nInheritance\n")


# class definition
class BaseClass():
    pass

    def get_name(self):
        return self.name;

    def set_name(self, name):
        self.name = name;
        pass


class SubClass(BaseClass):
    pass


a = SubClass()
a.set_name("abc")
print(a.get_name())
