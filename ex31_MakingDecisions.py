# ex31 Making Decisions

print "Do you want to go through Door#1 or Door#2?"

door = raw_input("> ")

if door == "1":
    print "Bear eating cheesecake. What do you do?"
    print "1. Eat cheesecake"
    print "2. Scream at the bear"

    bear = raw_input("> ")

    if bear == "1":
        print "Bear eats you"
    elif bear == "2":
        print "Bear eats you anyway"
    else:
        print "%s is a good choice" % bear

elif door == "2":
    print "You stare into endless abyss at X's retina."
    print "1. Blueberries"
    print "2. Yellow jacket"
    print "3. Revolvers"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Mind of jello"
    else:
        print "Pool of muck"

else:
    print "Fall on knife and die!"
