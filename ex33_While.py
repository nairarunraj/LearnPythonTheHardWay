# ex33 While loops


def populate_numbers(i, limit, step):
    numbers = range(i, limit + 1, step)

    return numbers

i = 0
numbers = []

while i < 6:
    print "At the top, i is %d" % i
    numbers.append(i)

    i += 1

    print "Numbers now - ", numbers
    print "At the bottom, i is %d" % i

print "The numbers: "

for num in numbers:
    print num

numbers = populate_numbers(0, 7, 2)

print "The numbers: "

for num in numbers:
    print num
