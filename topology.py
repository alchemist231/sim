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
	axis=util.Coordinate(Grid)
	que =util.BufferQueue(100)

	# print node.Node.count
	# print "mesh !",Grid.row_length
	if len(nodeList) == 0 :
		que.push(origin)
		visited=list(Grid.node_list)
		while node.Node.count != nodesCount or que.isEmpty:
			# print node.Node.count
			current = que.pop()
			if current not in Grid.node_list:
				createdNode = node.Node(current)
				addedNodeList.append(createdNode)
				Grid.place_node(createdNode)
				visited.append(current)
				if node.Node.count==nodesCount:
					break

				adjacent = axis.generate_adjacent_coordinate(current)[1]
				for each in adjacent:
					if each not in visited:
						que.push(each)
			

	return addedNodeList


def ring(Grid, origin , nodesCount, nodeList=[]):
	addedNodeList = []

	return addedNodeList


def star(Grid): 
	addedNodeList = []

	return addedNodeList