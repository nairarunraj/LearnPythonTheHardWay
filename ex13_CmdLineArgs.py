# ex13 Command Line Arguments

# import the module argv
from sys import argv

#First parameter is always the script name
script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third
