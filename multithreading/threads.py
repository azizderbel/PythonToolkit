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
    threads = [Thread(target=replace, args=(filename))
            for filename in filenames]

    # start the threads
    for thread in threads:
        thread.start()

    # wait for the threads to complete
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = perf_counter()

    main()
    # The program needs to wait for all non-daemon threads to complete before it can exit, even without join
    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')