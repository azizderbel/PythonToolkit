import time
import os
import multiprocessing
from PIL import Image, ImageFilter


filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]

def create_thumbnail(filename, size=(50,50),thumb_dir ='thumbs'):
    img = Image.open(filename)
    img = img.filter(ImageFilter.GaussianBlur())
    img.thumbnail(size)
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')
    print(f'{filename} was processed...')


if __name__ == '__main__':
    start = time.perf_counter()

    # create processes
    processes = [multiprocessing.Process(target=create_thumbnail, args=[filename]) 
                for filename in filenames]

    # start the processes
    for process in processes:
        process.start()

    # wait for completion
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')