class Node():

    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos
        self.f = 0
        self.g = 0 #distance from starting node
        self.h = 0 #distance from target node (heuristic)

    def __eq__(self, other):
        return self.pos == other.pos


def Astar(env, start, target):
    # Creating nodes for starting point and target point
    startNode = Node(None, start)
    startNode.f = 0
    startNode.g = 0
    startNode.h = 0
    targetNode = Node(None, target)
    targetNode.f = 0
    targetNode.g = 0
    targetNode.h = 0

    # Initialize list for OPEN AND CLOSED nodes
    openNodesList = []
    closedNodesList = []

    # Append starting point node to begin evaluations before loop
    openNodesList.append(startNode)

    # Loop until you find the target point
    while len(openNodesList) > 0:
        # Get current node to evaluate
        currentNode = openNodesList[0]
        currentNodeIndex = 0
        for nodeIndex, nodeItem in enumerate(openNodesList):
            if nodeItem.f < currentNode.f:
                currentNodeIndex = nodeIndex
                currentNode = nodeItem

        # Delete node from open nodes list and add it to closed nodes list
        openNodesList.pop(currentNodeIndex)
        closedNodesList.append(currentNode)

        # Found the target point
        if currentNode == targetNode:
            pathToTarget = []
            current = currentNode
            while current is not None:
                pathToTarget.append(current.pos)
                current = current.parent
            return pathToTarget[::-1] # path is from target to start. reverse before returning

        # Pinpoint neighbours
        neighbours = []
        for newPosition in [(-1, 0),(0, -1), (0, 1), (1, 0)]: # All 8 possible neighbours

            # Get node position
            nodePosition = (currentNode.pos[0] + newPosition[0], currentNode.pos[1] + newPosition[1])

            # Make sure within range
            if nodePosition[0] > (len(env) - 1) or nodePosition[0] < 0 or nodePosition[1] > (len(env[len(env)-1]) -1) or nodePosition[1] < 0:
                continue

            # Create new node
            newNode = Node(currentNode, nodePosition)

            # add to neighbours array
            neighbours.append(newNode)

        # Loop neighbours to find next current
        for neighbour in neighbours:

            # Check if neighbour is in the closed nodes list
            for closedNeighbour in closedNodesList:
                if neighbour == closedNeighbour:
                    continue

            # Create the f, g, and h values to evaluate later (f = g + h)
            neighbour.g = currentNode.g + 1
            neighbour.h = ((neighbour.pos[0] - targetNode.pos[0]) ** 2) + ((neighbour.pos[1] - targetNode.pos[1]) ** 2)
            neighbour.f = neighbour.g + neighbour.h

            # Check if neighbour is already in the open nodes list
            for open_node in openNodesList:
                if neighbour == open_node and neighbour.g > open_node.g:
                    continue

            # Add the neighbour to the open list for later evaluation
            openNodesList.append(neighbour)