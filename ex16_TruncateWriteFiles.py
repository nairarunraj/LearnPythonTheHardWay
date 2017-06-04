# ex16 Truncating and writing files

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# Truncate isn't needed when opening a file in the write mode
print "Truncating the file. Goodbye!"
target.truncate()

print "Enter three lines..."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "Close the file..."
target.close()
