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