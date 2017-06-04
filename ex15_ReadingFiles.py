# ex15 Reading files

from sys import argv

script, filename = argv

# open() returns a file object
txt = open(filename)

print "Here's your file %r: " % filename
print txt.read()

txt.close()

file_again = raw_input("Type the file again: > ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
