#!/usr/bin/env python3
# Which Car Should You Actually Drive?

suggestion = 'We recommend you should actually drive '
child = float(input("How many kids you have? "))

if child >= 8:
    suggestion = suggestion + 'School bus.'
elif child >= 6:
    suggestion = suggestion + 'Van.'
elif child >= 4:
    suggestion = suggestion + 'Full size SUV.'
elif child >= 2:
    suggestion = suggestion + 'Mid size SUV.'
else:
    suggestion = suggestion + 'Compact car.'
print(suggestion)
