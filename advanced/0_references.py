import ctypes
# variables are references that point to the objects in the memory.

# To find the memory address of an object referenced by a variable
counter = 584475
print(id(counter)) # base 10 number
print(hex(id(counter))) # hexadecimal representation
mem_add_counter = id(counter)

# An object in the memory address can have one or more references
max = counter
print(id(max)) # same Id
print(ctypes.c_long.from_address(mem_add_counter).value)

# if you assign a different value to the counter and max variables
# the number of references of the integer object with a value of 100 will be zero
# Once an object doesn’t have any reference, Python Memory Manager will destroy that object and reclaim the memory.
counter=None
max=None
print(ctypes.c_long.from_address(mem_add_counter).value)