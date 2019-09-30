import os
import glob
import shutil
import time


def main(source, destination):
        for filename in glob.glob(os.path.join(source, '*.*')):
        shutil.copy(filename, destination)


if __name__ == '__main__':
    start_time = time.time()
    main('/Oldfolder', '/Newfolder')
    print("--- %s seconds ---" % (time.time() - start_time))
