import time
def say():
    greeting = 'Hello'

    def display():
        print(greeting)

    return display  # dispaly func + nonlocal scope var is a closure

fn = say()
time.sleep(5) # even though the scope of the say function is gone we stil get access to its locally defined variables
fn()

