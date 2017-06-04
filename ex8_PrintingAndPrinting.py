# ex8 Printing and Printing

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ('one', 'two', "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

# As the third string contains a single quote, it will be shown in double quotes
# Other strings will be in single quotes
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
