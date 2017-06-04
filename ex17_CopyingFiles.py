# ex17 Copying files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#in_file = open(from_file)
#indata = in_file.read()

with open(from_file, 'r') as in_file:
    indata = in_file.read()

print "Input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, done"

out_file.close()
