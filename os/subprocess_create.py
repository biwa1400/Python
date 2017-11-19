import multiprocessing as mp
import os
import time

def whoami (what):
	print("Process %s says: %s" %(os.getpid(),what))

def count(name):
	whoami(name)
	start = 1
	stop = 10000
	for num in range(start,stop):
		print("Number %s of %s" %(num,stop))
		time.sleep(1)
	

if __name__ == "__main__":
	whoami("I'm main program")
	p = mp.Process(target = count, args=("count",))
	p.start()
	time.sleep(5)
	p.terminate()