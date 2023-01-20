countries = ['China','Spain','France']
c1,c2,c3 = countries # unpack all the the sequence items

# unpack specific items
colors = ['red', 'blue', 'green']
red, blue, *other = colors
# * pack the leftover elements into a new list
