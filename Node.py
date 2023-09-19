import megaMap as mp
import distanceMap

class Node:
    def __init__(self, orientation, index, nodeType):
        # Original Orientation
        self.original = orientation.copy()

        # Original Index
        self.index = index

        # Current Orientation
        self.orientation = orientation.copy()

        # Type of Node (Corner or Edge)
        self.nodeType = nodeType
    
    # Calculates our distance heuristic
    def grabHeuristic(self):
        if self.nodeType == 'Corner':
            # Distance from current to origin
            return distanceMap.cornerHash[(self.orientation[0], self.orientation[1], self.orientation[2])][(self.original[0], self.original[1], self.original[2])]
        else:
            # Distance from current to origin
            return distanceMap.edgeHash[(self.orientation[0], self.orientation[1])][(self.original[0], self.original[1])]

    # Rotate the node clockwise
    def rotateClockwise(self, color):
        # Create a new array
        newOrientation = []

        # Loop through the orientation, modify the item
        for item in self.orientation:
            if mp.adjacentFacesClockwise[color][item]:
                newItem = mp.adjacentFacesClockwise[color][item]
                newOrientation.append(newItem)

        # Set orientation to the new array
        self.orientation = newOrientation

    # Rotate the node counter clockwise
    def rotateCounterClockwise(self, color):
        # Create a new array
        newOrientation = []

        # Loop through the orientation, modify the item
        for item in self.orientation:
            if mp.adjacentFacesCounterClockwise[color][item]:
                newItem = mp.adjacentFacesCounterClockwise[color][item]
                newOrientation.append(newItem)

        # Set orientation to the new array
        self.orientation = newOrientation
    
    # Grabs the node's orientation to use in printing the megaminx
    def grabColor(self, color):
        for i, value in enumerate(self.orientation):
            if value == color:
                return self.original[i]