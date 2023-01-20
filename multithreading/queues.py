from queue import Queue
# allows you to exchange data safely between multiple threads

# store up to 10 items
queue = Queue(maxsize=10)

# how many items are stored in the queue
print(queue.qsize()) # empty() and full() are available
