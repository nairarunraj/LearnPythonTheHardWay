# ex38 ListModification

#################
# You use a list whenever you have something that matches the list data structure's useful features:
#    If you need to maintain order. Remember, this is listed order, not sorted order. Lists do not sort for you.
#    If you need to access the contents randomly by a number. Remember, this is using cardinal numbers starting at 0.
#    If you need to go through the contents linearly (first to last). Remember, that's what for-loops are for.
#################

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Not actually 10 things. Fix it"

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()  # Pops the last element from the list
    print "more_stuff- ", more_stuff
    print "Adding ", next_one
    stuff.append(next_one)

    print "There are %d items now" % len(stuff)

print "Stuffs - ", stuff

print "Let's do something with stuff"

print stuff[1]  # 2nd element
print stuff[-1]  # last element
print stuff.pop()  # Pops the last element
print ' '.join(stuff)  # Space separated string
print '#'.join(stuff[3:5])  # Elements 3 and 4 are sliced
