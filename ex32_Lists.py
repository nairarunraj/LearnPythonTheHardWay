# ex32 Lists

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'mangoes', 'pears']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# going through a List
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type %s" % fruit

# also, we can go through mixed Lists
# use %r because it can be either a string or a number
# %s works too btw
for i in change:
    print "I got %s" % i

# Building lists
elements = []

# use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list" % i
    elements.append(i)

# Easier way to assign a range
elements = range(0, 6)

# print the elements
for i in elements:
    print "Element - %d" % i
