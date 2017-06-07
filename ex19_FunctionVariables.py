# ex19 Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket\n"

print "We can just give the functions numbers directly:"
cheese_and_crackers(10,20)

print "Or, we can use variables from our script:"
amount_of_cheese = 20
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can do maths inside too: "
cheese_and_crackers(10+23, 5+6)

print "And we can combine the two, variables and maths: "
cheese_and_crackers(amount_of_cheese+44, amount_of_crackers+888)
