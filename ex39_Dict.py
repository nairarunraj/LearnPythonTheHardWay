# ex39 Dictionary

# Dictionaries aren't ordered
# For an ordered dictionary, use collections.OrderedDict

states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY state has ", cities['NY']
print "OR state has ", cities['OR']

print '-' * 10
print "Michigan's abbr is ", states['Michigan']
print "Florida's abbr is ", states['Florida']

print '-' * 10
print "Michigan has ", cities[states['Michigan']]
print "Florida has ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbr in states.items():
    print "%s is abbreviated %s" % (state, abbr)

# print every city in the state
for abbr, city in cities.items():
    print "%s has the city %s" % (abbr, city)

# now, do both at the same time
for state, abbr in states.items():
    print "%s state is abbreviated %s and has the city %s" % (
        state, abbr, cities[abbr])

print '-' * 10
state = states.get('Texas')

if not state:
    print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', "Doesn't exist")
print "The city for the state 'TX' is: %s" % city
