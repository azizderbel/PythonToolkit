# A function contains at least one yield statement, it’s a generator function.

# When you call a generator function, it returns a generator object, which is also an iterator.

# When you call a generator function, it returns a new generator object. However, it doesn’t start the function.

def squares(length):
    for n in range(length):
        yield n ** 2

# generator expression provides you with a more simple way to return a generator object

squares = (n** 2 for n in range(5))