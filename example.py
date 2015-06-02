from multiprocessing import Process, Value
from time import time

def add(x):
    x.value += 1

def add2(x):
    for i in range(100):
        x.value += 1

if __name__ == '__main__':
    x = Value("i", 0)

    start = time()

    for i in range(100):
        p = Process(target=add, args=(x,))
        p.start()
        p.join()
    
    print("Took", time()-start, "x", x.value) #0.43 seconds to set x to 100
    
    x = Value("i", 0)

    start = time()

    p = Process(target=add2, args=(x,))
    p.start()
    p.join()
    
    print("Took", time()-start, "x", x.value) #0.005 seconds to set x to 100
    
    #Creating processes takes a long time! Try to run as much as you can in as few processes as possible.
