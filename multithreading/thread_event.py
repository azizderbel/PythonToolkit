# The Event class offers a simple but effective way to coordinate between threads
# Threads that share an Event object can check if the event is set, set the event, unset the event, or wait for the event to be set.

from threading import Event,Thread
from time import sleep

def task(event: Event, id: int) -> None:
    print(f'Thread {id} started. Waiting for the signal....')
    event.wait()
    print(f'Received signal. The thread {id} was completed.')

def main() -> None:

    # The event is not set per default
    event = Event()

    t1 = Thread(target=task, args=(event,1))
    t2 = Thread(target=task, args=(event,2))

    t1.start()
    t2.start()
    # The 2 threads starts and waits for the event to be set

    print('Blocking the main thread for 3 seconds...')
    sleep(3)
    # the event object will be set after 3 secs
    event.set()

if __name__ == '__main__':
    main()
