# ex5 Printing using formatters

name = 'Arunraj Nair'
age = 28
height = 165
weight = 62
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about this %s." % name
print "He's %d cms tall" % height
print "He's %d kgs heavy" % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

print "If I add %d, %d, and %d I get %d" % (age, height, weight, age+height+weight)
