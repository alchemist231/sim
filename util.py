import math


"""======================================================================================
							Utility Classes
======================================================================================"""



class Coordinate:

	directions = ('north','south','east','west')

	def __init__(self,Grid):
		self.column = Grid.column_length
		self.row = Grid.row_length
		self.current = {'north':(False),'south':(False),'east':(False),'west':(False)}
		# print self.row,self.column
		# print "-"*90

	def generateAdjacentCoordinate(self, coordinate):
		x,y = coordinate
		north = (x,y+1)
		south = (x,y-1)
		east  = (x+1,y)
		west  = (x-1,y)
		adjacent = [north,south,east,west]
		adjacent_nodes = []

		i=0
		for each in adjacent :
			if self.validate(each)==True:
				self.current[Coordinate.directions[i]] = each
				adjacent_nodes.append(each)
			i += 1
		return (self.current,adjacent_nodes)

	def validate(self, coordinate):
		x,y = coordinate
		if x>self.row-1 or x<0 or y>self.column-1 or y<0 :
			# print "validation false",(x,y)
			return False
		return True

class BufferQueue :

	def __init__(self,size):
		self.buffer_size = size
		self.buffer = []

	def push(self,value):
		if self.bufferFull() :
			print "Current Buffer --> "
			self.printBuffer()
			raise BufferError("Buffer Overflow")
		elif value not in self.buffer :
			self.buffer.insert(0,value)

	def bufferFull(self):
		return len(self.buffer) == self.buffer_size

	def pop(self):
		if self.isEmpty() :
			raise BufferError("Buffer Empty")
		else :
			return self.buffer.pop()

	def firstElement(self):
		if self.isEmpty() != True :
			return self.buffer[0]

	def isEmpty(self):
		return len(self.buffer) == 0

	def printBuffer(self):
		for each in self.buffer :
			print each,




"""======================================================================================
							Utility Functions
======================================================================================"""

def euclideanDistance(point1,point2):
	x1,y1 = point1
	x2,y2 = point2
	return math.sqrt((x1-x2)**2+(y1-y2)**2)

def manhattanDistance(point1,point2):
	x1,y1 = point1
	x2,y2 = point2
	return abs(x1-x2)+abs(y1-y2)







