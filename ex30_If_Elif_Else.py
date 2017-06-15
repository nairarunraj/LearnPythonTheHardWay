# ex30 If-elif-else

people = 30
cars = 40
trucks = 15

if cars > people:
    print "Take cars"
elif cars < people:
    print "Shouldn't take cars"
else:
    print "Can't decide"

if trucks > cars:
    print "Too many trucks"
elif trucks < cars:
    print "Take the trucks"
else:
    print "Still can't decide"

if people > trucks:
    print "Fine, take the trucks"
else:
    print "Stay home"
