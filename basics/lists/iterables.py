# In Python, an iterable is an object that includes zero, one, or many elements. An iterable has the ability to return its elements one at a time.

#lists,tuples,strings... are all iterables

str = 'Iterables'
for ch in str:
    print(ch)

# An iterable can be iterated over. And an iterator is the agent that performs the iteration.
# an iterable provides an iterator so that we can iterate over

# get the iterator from iterable
colors = ['red', 'green', 'blue']
colors_iter = iter(colors)
item = next(colors_iter) # start iteration




