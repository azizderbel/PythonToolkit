person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
    }


# access items
print(person['first_name'])
# to to avoid error
print(person.get('agee')) # None

# add or mod an entry
person['new'] = 15

# delete an entry
del person['new']

# loop through
list1 = person.items() # list of tuples
for key, value in person.items():
    print(f"{key}: {value}")

for key in person.keys():
    print(key)

for value in person.values():
    print(value)
