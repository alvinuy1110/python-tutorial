#####
# This is the Exception Handling tutorial
#####
title = "Exception Handling Tutorial"
print(title)

# Reference https://docs.python.org/3/library/exceptions.html#bltin-exceptions

# Basic
try:
    x = int("11a")
except ValueError:
    print("Oops!  That was no valid number.  Try again...")

# assertion test
try:
    assert 1 < 0
except AssertionError:
    print("AssertionError")


# Raising an error
# keyword 'raise' is similar to throw
class MyException(Exception):
    pass


try:
    if 1 < 10:
        raise MyException("blah")
except Exception as err:
    # print(err.with_traceback())
    print(type(err))  # the instance
    print(err.args)  # the arguments if any
    pass
else:  # only called when no exception
    print("last step")

# rethrowing error, use the raise keyword

try:
    if 1 < 10:
        raise MyException("blah")
except Exception as err:
    # print(err.with_traceback())
    print(type(err))  # the instance
    print(err.args)  # the arguments if any
    # raise
else:  # only called when no exception
    print("last step")

# Finally keyword
try:
    raise KeyboardInterrupt
finally:
    print("print me always")

