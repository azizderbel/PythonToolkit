# In Python, there’re two main kinds of errors: syntax errors and exceptions.
# Even though when your code has valid syntax, it may cause an error during execution.
# In Python, errors that occur during the execution are called exceptions
#In Python, exceptions have different types such as TypeError, NameError, etc.
try:
    # code that may cause errors
    pass
except TypeError:
    # code that handle exception1
    pass
except NameError:
    # code that handle exception2
    pass
except Exception:
    # code that handle any other exception
    pass
else: #(optional)
    # code that executes when no exception occurs
    pass
finally: #(optional)
    # executes after the else section
    pass

fruits = {
    'apple': 10,
    'orange': 20,
    'banana': 30
}

key = None
while True:
    try:
        key = input('Enter a key to lookup:')
        fruit = fruits[key.lower()]
    except KeyError:
        print(f'Error! {key} does not exist.')
    except KeyboardInterrupt:
        break
    else:
        print(fruit)
    finally:
        print('Press Ctrl-C to exit.')