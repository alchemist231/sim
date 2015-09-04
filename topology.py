"""
Define all topoligies as function
A call to this file will make use of setup of topology
Following call in different files, will do the following actions
import topology
	dir(topology) --> return string of functions
"""

"-----------------------------------------------------------------------------------------------------"
import search
import util
import node
# from simulationSetup import Coordinate
# import coordinate


def mesh(Grid, origin, nodesCount, nodeList=[], reset=False):
	addedNodeList = []
	x_dim,y_dim = Grid.dimensions()
	axis=util.Coordinate(Grid)
	que =util.BufferQueue(x_dim*y_dim)
	maximumPossibleNodes = nodesCount + len(Grid.nodeList())

	if len(nodeList) == 0 :

		if x_dim*y_dim < maximumPossibleNodes :
			raise NameError("Maximum possible number of nodes in network " + str(x_dim*y_dim)+ " , "+ str(maximumPossibleNodes)+" provided!")

		que.push(origin)
		visited=[]
	
		while node.Node.count != maximumPossibleNodes  or que.isEmpty:
			current = que.pop()
			if current not in Grid.nodeList():
				createdNode = node.Node(current)
				addedNodeList.append(createdNode)
				Grid.placeNode(createdNode)
				visited.append(current)
				if node.Node.count==maximumPossibleNodes:
					break

			adjacent = axis.generateAdjacentCoordinate(current)[1]
			for each in adjacent:
				if each not in visited:
					que.push(each)
		

	return addedNodeList

def meshAppend(Grid, origin, nodesCount, nodeList=[], reset=False):
	""""""


def ring(Grid, origin , nodesCount, nodeList=[]):
	addedNodeList = []

	return addedNodeList


def star(Grid): 
	addedNodeList = []

	return addedNodeList