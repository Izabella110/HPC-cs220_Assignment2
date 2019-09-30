import os
import shutil
import time
import threading
from threading import Thread
import glob



def func(source, destination):
    for file0 in glob.glob(os.path.join(source, '*.*')):
        shutil.copy(file0, destination)


def main(source, destination):
    thread: Thread = threading.Thread(target=func, args=(source, destination))
    thread.start()


if __name__ == '__main__':
    start_time = time.time()
    main('/Oldfolder', '/Newfolder')
    print("--- %s seconds ---" % (time.time() - start_time))v