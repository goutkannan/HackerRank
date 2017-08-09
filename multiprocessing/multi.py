import multiprocessing 

def spawn(num):
    print("Spawn {}".format(num))

if __name__=='__main__':
    for i in range(20):
        p = multiprocessing.Process(target=spawn,args=(i,))
        p.start()
        #p.join()

