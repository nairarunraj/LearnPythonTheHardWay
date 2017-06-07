# ex21 Calculator

def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Let's do some maths with just functions!"

age = add(20, 5)
height = subtract(170,10)
weight = multiply(30, 2)
iq = divide(100, 2)

print "Age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)

print "Here's a puzzle"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes ", what, ". Can you do it by hand?"
