import threading
import numpy as np
import time
import random

class roomsThread(threading.Thread):
	def __init__(self,high,rooms):
		super(roomsThread, self).__init__()
		self.high=high
		self.porprete = 0
		self.total=0
		self.choices = ["b", "bp", "p", "p", "p", "p","v", "v", "v", "v", "v", "v", "v", "v", "v", "v"]
		self.rooms = rooms

	def run(self):
		while self.total < self.high:
			self.total+=1
			timeToWait = random.randrange(1,2)
			time.sleep(timeToWait)
			self.rooms[random.randrange(0,4),random.randrange(0,4)] = random.choice(self.choices)
			print(self.rooms)

	def getChoice(self, position, rooms):
		return rooms[int(position / 10)][position % 10]
	
	def cherche_but(self, rooms):
		for x in range(5):
			for y in range(5):
				if(rooms[x][y] != "v"):
					pos = int(str(x) + str(y))
					return pos
		return -11


