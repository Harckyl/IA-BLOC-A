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

	def run(self, rooms):
		while self.total < self.high:
			self.total+=1
			timeToWait = random.randrange(1,2)
			time.sleep(timeToWait)
			rooms[random.randrange(0,4),random.randrange(0,4)] = random.choice(self.choices)
			res = self.getChoice(11, rooms)
			print(rooms)

	def getChoice(self, position, rooms):
		return rooms[int(position / 10), position % 10]


