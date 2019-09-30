import os
import shutil
import time
import multiprocessing
import glob


def func(source, destination):
    for filename in glob.glob(os.path.join(source, '*.*')):
        shutil.copy(filename, destination)


def main(source, destination):
    proc = multiprocessing.Process(target=func, args=(source, destination))
    proc.start()


if __name__ == '__main__':
    start_time = time.time()
    main('/Oldfolder', '/Newfolder')
    print("--- %s seconds ---" % (time.time() - start_time))
