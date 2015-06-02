# Python Process Time Test
Simple demonstration as to why you should put as much code into as few processes as possible

For example, let's say you have the below code

```python
def complexFunction():
  operationOne()
  operationTwo()

for i in range(100):
  complexFunction()
```

You decide to speed up the code by making it multiprocess

Try to *avoid* doing this:

```python
def complexFunction():
  p1 = Process(target=operationOne)
  p2 = Process(target=operationTwo)
  p1.start()
  p2.start()
  p1.join()
  p2.join()

for i in range(100):
  complexFunction()
```

And instead do this

```python
def complexFunction():
  operationOne()
  operationTwo()

def myThread():
  for i in range(50):
    complexFunction()

p1 = Process(target=myThread)
p2 = Process(target=myThread)
p1.start()
p2.start()
p1.join()
p2.join()
```

They both run complexFunction 100 times, the difference is the second one only creates a new Process twice, the first one created a new Process 200 times!  Simple working example:

```python
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
	
	print("Took", time()-start,"x",x.value) #0.43 seconds to set x to 100
	
	x = Value("i", 0)

	start = time()

	p = Process(target=add2, args=(x,))
	p.start()
	p.join()
	
	print("Took", time()-start,"x",x.value) #0.005 seconds to set x to 100
	
	#Creating processes takes a long time! Try to run as much as you can in as few processes as possible.
```
