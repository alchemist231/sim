import topology
import search



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
		self.node_list = []


	def get_node(self,coordinate):
		x , y = coordinate
			if self.grid[x][y] == 0:
				if debug == True : print "No node present at",coordinate
				return False
		return self.grid[x][y]

	def initialize_node(self, node):
		x,y = node.coordinate
		if self.node_present[x][y]:
			if debug == True : print "Initialization Failed, Node already exists at", (x,y)
			return False
		else :
			self.grid[x][y] = node
			self.node_present[x][y] = True
			self.node_list.append((x,y))
		return True

	def get_node_list(self):
		return self.node_list

	def reset(self):
		self.grid = [[0 for i in range(0,column_length)] for j in range(0,row_length)]
		self.node_present = [[False for i in range(0,column_length)] for j in range(0,row_length)]
		self.node_list = []
		if debug == True : print "Grid Reset"


	def __str__(self):
		for x in range(0,self.row_length):
			for y in range(0,self.column_length):
				if self.node_present[self.row_length-1-x][self.column_length-1-y] == True:
					print 'X',
					if y == (self.column_length-1):
						print '\n'
				else :
					if y == (self.column_length-1):
						print '\n'
					else :
						print '-',




class Coordinate:

	def __init__(self,Grid):
		self.column = Grid.column_length
		self.row = Grid.row_length

	def generate_adjacent_nodes(self, coordinate):
		x,y = coordinate
		north = (x,y+1)
		south = (x,y-1)
		east  = (x+1,y)
		west  = (x-1,y)
		adjacent = [north,south,east,west]
		adjacent_node = []
		for each in adjacent :
			if validate(each)==True:
				adjacent_node.append(each)
		return each



class Graph:


class Topologies:
	""" This class defines various topolgies, and executes node placements according to the different Topologies
		Default call of topology generates node, places on empty grid, assigns node to Grid, returns Grid
		Invokes function from topology.py
	"""

	def __init__(self, Grid, set_topology='mesh' , origin=(0,0) , number_of_nodes = 0, nodeList = []) :
		self.nodeList = nodeList
		if set_topology not in dir(topology):
			raise AttributeError, set_topology + " not found !"
		else :
			getattr(topology,set_topology)(Grid , origin ,number_of_nodes, nodeList)
		self.currentTopology = [set_topology]

	def get_topology(self):
		return self.currentTopology

	def add_topology(self, Grid, additionalTopology='mesh', origin=(0,0), number_of_nodes = 0, nodeList = []):
		if additionalTopology not in dir(topology):
			raise AttributeError, set_topology + " not found !"
		else :
			self.nodeList += getattr(topology,additionalTopology)(Grid , origin , number_of_nodes, nodeList)
			if additionalTopology not in self.currentTopology:
				self.currentTopology.append(additionalTopology)

	def modify_topology(self, Grid, newTopology='mesh', origin=(0,0), number_of_nodes = 0, additionalNodeList=[]):
		## modify current configuration to different configuration using self.nodeList
		add_topology(Grid,self.currentTopology,origin,additionalNodeList)
		self.currentTopology = [newTopology]
		self.nodeList = getattr(topology,newTopology)(Grid , origin ,number_of_nodes, nodeList, True)




		








# define in node.py
class Node:

self.node_count=0





