import topology
import search
import node

debug=False

class Grid:
	"""
	This class defines a grid , with some coordinates being nodes
	Placement of such nodes ( topology control ) will help evaluate optimal
	routing for various topolgies with heterogenous data flow

	Execution: A 2-dimensional array of objects backed by a list of lists. 
			   Data is accessed via grid[x][y] where (x,y) are node positions with 
			   x horizontal, y vertical and the origin (0,0) in the bottom left corner.

	The __str__ method constructs an output that is oriented like a network layout

	"""

	def __init__(self, row_length , column_length ):
		# Initialize grid with 0 , else place node objects at different location
		self.grid = [[0 for i in range(0,column_length)] for j in range(0,row_length)]
		self.node_present = [[False for i in range(0,column_length)] for j in range(0,row_length)]
		self.column_length = column_length
		self.row_length = row_length
		self.node_list = ()


	def getNode(self,coordinate):
		x,y = coordinate
		if self.grid[x][y] == 0:
			if debug == True : print "No node present at",coordinate
			return False
		return self.grid[x][y]

	def placeNode(self, node):
		x,y = node.coordinate
		# print "place",(x,y)
		if self.node_present[x][y]:
			if debug == True : print "Initialization Failed, Node already exists at", (x,y)
			return False
		else :
			self.grid[x][y] = node
			self.node_present[x][y] = True
			self.appendNodeList((x,y))
		return True

	def appendNodeList(self,coord):
		self.node_list=list(self.node_list)
		self.node_list.append(coord)
		self.node_list=tuple(self.node_list)

	def nodePresent(self,coord):
		x,y = coord
		return self.node_present[x][y]


	def nodeList(self):
		return self.node_list

	def reset(self):
		self.grid = [[0 for i in range(0,column_length)] for j in range(0,row_length)]
		self.node_present = [[False for i in range(0,column_length)] for j in range(0,row_length)]
		self.node_list = []
		if debug == True : print "Grid Reset"

	def dimensions(self):
		return (self.row_length,self.column_length)


	def __str__(self):
		print "-"*self.column_length*10,'\n','\n'
		for x in range(0,self.row_length):
			for i in range(0,1): print '\t',
			for y in range(0,self.column_length):
				if self.node_present[self.row_length-1-x][y] == True:
					print 'X','\t',
					if y == (self.column_length-1):
						print '\n'
				else :
					print '-','\t',
					if y == (self.column_length-1):
						print '\n'
		print "-"*self.column_length*10,'\n','\n'





class Topologies:
	""" This class defines various topolgies, and executes node placements according to the different Topologies
		Default call of topology generates node, places on empty grid, assigns node to Grid, returns Grid
		Invokes function from topology.py
	"""

	def __init__(self, Grid, set_topology='mesh' , origin=(0,0) , number_of_nodes = 0, nodeList = []) :
		self.nodeList = nodeList
		if set_topology not in dir(topology):
			raise AttributeError,(str(set_topology) + " not found !")
		else :
			getattr(topology,set_topology)(Grid , origin ,number_of_nodes, nodeList)
		self.currentTopology = [set_topology]

	def getTopology(self):
		return self.currentTopology

	def addTopology(self, Grid, additionalTopology='mesh', origin=(0,0), number_of_nodes = 0, nodeList = []):
		if additionalTopology not in dir(topology):
			raise AttributeError, set_topology + " not found !"
		else :
			self.nodeList += getattr(topology,additionalTopology)(Grid , origin , number_of_nodes, nodeList)
			if additionalTopology not in self.currentTopology:
				self.currentTopology.append(additionalTopology)

	def modifyTopology(self, Grid, newTopology='mesh', origin=(0,0), number_of_nodes = 0, additionalNodeList=[]):
		## modify current configuration to different configuration using self.nodeList
		add_topology(Grid,self.currentTopology,origin,additionalNodeList)
		self.currentTopology = [newTopology]
		self.nodeList = getattr(topology,newTopology)(Grid , origin ,number_of_nodes, nodeList, True)






class Graph :

	def __init__(self,Grid):
		axis = util.Coordinate()





g=Grid(9,5)
t=Topologies(g,number_of_nodes=35)
g.__str__()
t.addTopology(g,number_of_nodes=1)
g.__str__()
t.addTopology(g,number_of_nodes=3)
g.__str__()

# print "-"*100
# print g.node_list
# print "-"*100

print node.Node.count









# define in node.py
# class Node:

# self.node_count=0





