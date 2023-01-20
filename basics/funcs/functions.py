def test():
    """
    docstring

    """
    pass

test() # call the function
# return None per default

def test_one(param_one = 0): # defualt value
    pass

test_one(param_one = 5)


# Functions that accept a function example
def get_full_name(name,last_name,formatter):
    return formatter(name,last_name)


def get_full_name(name,last_name,formatter):
    return formatter(name,last_name)

full_name = get_full_name(
    'aziz',
    'derbel',
    lambda first_name,last_name: f"{first_name} {last_name}")