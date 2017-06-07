# ex18 Functions

# like argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %s, arg2: %s" % (arg1, arg2)

# args is pointless, we can do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# just one argument
def print_one(arg1):
    print "arg1: %s" % arg1

# no arguments
def print_none():
    print "I got nothing"

print_two("Arun", "Nair")
print_two_again("Arunraj", "Nair")
print_one("First!")
print_none()
