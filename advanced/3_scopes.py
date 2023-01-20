# Python has a built_n scopre that encloses all modules global scopes
counter = 10

# we can retreive the value of a global var from inside the function
# but we can not modified unless we use the global key word
def reset():
    global counter
    counter = 88
    print(counter) # 0


reset()

print(counter) # 0
