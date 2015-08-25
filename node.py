import util

class Node:

	count = 0
	node_dict={}
	nodeId = []

	def __init__(self,  coordinate = None, node_id =0, bufferSize = 20):
		"""
		self.id
		self.coordinate
		self.neighbours
		self.state = True/False --> Working / Faulty
		self.buffer = util.BufferQueue
		"""
		if coordinate == None :
			raise NameError("coordinate missing in node instantiation")

		if node_id != 0:
			if node_id not in node_dict.key():
				Node.count += 1
				self.id = node_id
				Node.node_dict[node_id] = self
				Node.nodeId.append(nodeId)
			else:
				if debug == True : print " Node ",node_id,"already exists!"
		else :
			self.id = Node.count
			Node.count += 1
			Node.node_dict[self.id] = self

		self.coordinate = coordinate
		self.neighbours = ()
		self.state      = True
		self.bufferSize = bufferSize
		self.buffer     = util.BufferQueue(self.bufferSize)

	def get_id(self):
		return self.id

	def set_neighbours(self, neighbours):
		self.neighbours = list(self.neighbours)
		self.neighbours = neighbours
		self.neighbours = tuple(self.neighbours)
		if debug == True : print " Neighbours of",self.coordinate,' :',self.neighbours

	def get_neighbours(self):
		return self.neighbours

	def set_fault(self):
		self.state = False


# class Flit:

# 	def __init__(self):



# n1=Node()
# n2=Node()
# n3=Node()

# print n1.id,n2.id,n3.id