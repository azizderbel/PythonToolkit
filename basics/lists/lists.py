# define a list
list1 = [0,2,2,3,4]
list2 = list([1,2])
print(len(list2)) # 2

# access items
print(list1[0]) # first item
print(list1[1]) # last item

# slicing
print(list1[0:3])

# iterate over
for item in list1:
    #print(item)
    pass

for index,item in enumerate(list1):
    #print(f'index={index} item={item}')
    pass

# 2 lists simultanously
for a,b in zip(list2,list2):
    print(a)
    print(b)

# add items at the end
list1.append('aziz')

# add items at any position
list1.insert(1,6)

# delete an element
list1.remove('aziz')

# delete at index
list1.pop(-1)

# reverse order (in place)
list1.reverse()

# sort in place
list1.sort(reverse=False)

# return sorted copy
aux = sorted(list1)

# search an item (index number of first occur)
index = list1.index(2)  #value error is raised if not found


x = [0,2,3,5,4,8]
# sort list in place
x.sort(reverse=True)

companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

# order by company salary
companies.sort(key=lambda company: company[2])



# Map Function
bonuses = [100, 200, 300]
iterator = map(lambda bonus: bonus*2, bonuses)

# Apply Filters
scores = [70, 60, 80, 90, 50]
filtered = filter(lambda score: score >= 70, scores)


# List comprehension
numbers = [1, 2, 3, 4, 5]
#equivalent of map
squares = [number**2 for number in numbers]
#equivalent of map + filter
mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

highest_mountains = [m for m in mountains if m[1] > 8600]

# ************************* TUPLES

# TYPLES ARE IMMUTABLE list
numbers = (3,)
string = tuple([1])
print(type(numbers) is tuple)