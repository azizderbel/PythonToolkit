# By definition, daemon threads are background threads.
# use cases
# Log information to a file in the background.
# Scrap contents from a website in the background.
# Auto-save the data into a database in the background.

from threading import Thread
from time import perf_counter,sleep

def replace(id):
    sleep(5)
    print(f"thread{id}")

def main():
    filenames = [
        '1',
        '2',
    ]

    # create threads
    threads = [Thread(target=replace, args=(filename),deamon=True)
            for filename in filenames]

    # start the threads
    for thread in threads:
        thread.start()


if __name__ == "__main__":
    start_time = perf_counter()

    main()
    # The program terminates because it doesn’t need to wait for the daemon thread to complete. Also, the daemon thread is killed automatically when the program exits.
    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')