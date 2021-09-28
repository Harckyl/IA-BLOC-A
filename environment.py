import threading
import numpy as np
import time
import random

class roomsThread(threading.Thread):
	def __init__(self,high):
		super(roomsThread, self).__init__()
		self.high=high
		self.total=0
		self.choices = ["b", "bp", "p", "p", "p", "p"]

	def run(self):
		while self.total < self.high:
			self.total+=1
			timeToWait = random.randrange(5,12)
			time.sleep(timeToWait)
			rooms[random.randrange(0,4),random.randrange(0,4)] = random.choice(self.choices)
			res = self.getChoice(11)
			print(rooms)

	def getChoice(self, position):
		return rooms[int(position / 10), position % 10]


rooms = np.full((5,5),"v")
print(rooms)
maxRep = 5
environment = roomsThread(maxRep)
environment.start() # This actually causes the thread to run
environment.join()  # This waits until the thread has completed



print("DONE")