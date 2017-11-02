"""
Sample program to show multi processing
"""
import time
import multiprocessing
def spawn(num):
    """ Thread Client """
    time.sleep(2)
    print("Spawn {}".format(num))

if __name__ == '__main__':
    for i in range(20):
        p = multiprocessing.Process(target=spawn, args=(i, ))
        p.start()
        #p.join()
