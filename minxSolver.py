import random, time, heapq, copy, json
import megaMap as mp
import distanceMap
from faceControl import Face

# The printing characterization
upwardPrint = mp.megaPrintUpward
downwardPrint = mp.megaPrintDownward

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

class Minx:
    def __init__(self, root, parent, depth=0, color=None):
        # Root Minx
        self.root = root

        # Parent Minx
        self.parent = parent

        # List of Corner Nodes and Edge Nodes
        self.edges = []
        self.corners = []

        # Our Depth G(Minx)
        self.depth = depth

        # Our total heuristic
        self.fValue = 0
        self.fNode = None

        # What color did we rotate by?
        self.color = color

        # Our list of Faces
        self.faceList = []

    def __lt__(self, other):
        return self.fValue < other.fValue

    def populateNodes(self):
        # Grab our list
        starterEdges = mp.starterEdges
        starterCorners = mp.starterCorners

        # Populate our Corners
        # newNode = Node(['Red', 'Green', 'White'], 0, 'Corner')
        for i in range(20):
            newNode = Node(starterCorners[i], i, 'Corner')
            self.corners.append(newNode)

        # Populate our Edges
        # newNode = Node(['Red', 'Green'], 0, 'Edge')
        for i in range(30):
            newNode = Node(starterEdges[i], i, 'Edge')
            self.edges.append(newNode)

    def rotateClockwise(self, color):
        # Grab which node indexes within corners and edges need to be rotated
        cornerRotation = mp.minxCorners[color]
        edgeRotation = mp.minxEdges[color]

        # Update their indexes
        self.corners[cornerRotation[0]], self.corners[cornerRotation[1]], self.corners[cornerRotation[2]], self.corners[cornerRotation[3]], self.corners[cornerRotation[4]] = self.corners[cornerRotation[4]], self.corners[cornerRotation[0]], self.corners[cornerRotation[1]], self.corners[cornerRotation[2]], self.corners[cornerRotation[3]]
        self.edges[edgeRotation[0]], self.edges[edgeRotation[1]], self.edges[edgeRotation[2]], self.edges[edgeRotation[3]], self.edges[edgeRotation[4]] = self.edges[edgeRotation[4]], self.edges[edgeRotation[0]], self.edges[edgeRotation[1]], self.edges[edgeRotation[2]], self.edges[edgeRotation[3]]

        # Inform the node to rotate orientation
        for i in range(5):
            self.corners[cornerRotation[i]].rotateClockwise(color)
            self.edges[edgeRotation[i]].rotateClockwise(color)

    def rotateCounterClockwise(self, color):
        # Grab which node indexes within corners and edges need to be rotated
        cornerRotation = mp.minxCorners[color]
        edgeRotation = mp.minxEdges[color]

        # Update their indexes
        self.corners[cornerRotation[0]], self.corners[cornerRotation[1]], self.corners[cornerRotation[2]], self.corners[cornerRotation[3]], self.corners[cornerRotation[4]] = self.corners[cornerRotation[1]], self.corners[cornerRotation[2]], self.corners[cornerRotation[3]], self.corners[cornerRotation[4]], self.corners[cornerRotation[0]]
        self.edges[edgeRotation[0]], self.edges[edgeRotation[1]], self.edges[edgeRotation[2]], self.edges[edgeRotation[3]], self.edges[edgeRotation[4]] = self.edges[edgeRotation[1]], self.edges[edgeRotation[2]], self.edges[edgeRotation[3]], self.edges[edgeRotation[4]], self.edges[edgeRotation[0]]

        # Inform the node to rotate orientation
        for i in range(5):
            self.corners[cornerRotation[i]].rotateCounterClockwise(color)
            self.edges[edgeRotation[i]].rotateCounterClockwise(color)

    def calculateHeuristic(self):
        # Maximum Node
        maxNode = self.edges[0]
        maxValue = self.edges[0].grabHeuristic()

        # Grab the Edges
        for i in self.edges:
            testValue = i.grabHeuristic()
            if maxValue < testValue:
                maxNode = i
                maxValue = testValue
        for i in self.corners:
            testValue = i.grabHeuristic()
            if maxValue < testValue:
                maxNode = i
                maxValue = testValue
        
        # Update our max value
        self.fValue = self.depth + maxValue
        self.fNode = maxNode

    # Used to print the megaminx out to HTML
    def printMinx(self, versionControl):

        # Populate our Faces
        for i in upwardPrint:
            newFace = Face(i, 'Up')
            self.faceList.append(newFace)
        for i in downwardPrint:
            newFace = Face(i, 'Down')
            self.faceList.append(newFace)
        
        # Our dump file for the HTML to update
        newDump = {}
        newDump['Version'] = versionControl
        newDump['Colors'] = {}

        # Grab all the components of every face
        for i in self.faceList:
            i.updateColor(self.corners, self.edges)
            newDump['Colors'][i.color] = i.components.copy()

        # Open our json file and dump it by writing to it!
        with open('components.json', 'w') as f:
            json.dump(newDump, f)
        
        # Clear our faceList as we no longer need to update
        self.faceList.clear()

def AStar(root):
    # Create a priority queue
    priorityQueue = []

    # Number of expanded nodes
    expansionCount = 0

    # Grabs the smallest fValue
    heapq.heappush(priorityQueue, (root.fValue, root))

    # Check when you pop the Priority Queue
    while len(priorityQueue) > 0:
    
        # Grab the minimum fValue
        currentMinx = heapq.heappop(priorityQueue)

        # Increment the number of expanded nodes
        expansionCount += 1

        # Check H-Value != 0, if == 0 then break and return
        hValue = currentMinx[1].fValue - currentMinx[1].depth
        if hValue == 0:
            return currentMinx[1], expansionCount
        
        # Add 12 new children to Priority Queue
        for i in range(12):
            # Copy the Minx 
            newMinx = copy.deepcopy(currentMinx[1])
            
            # Increase depth G(value) by 1
            newMinx.depth = currentMinx[1].depth+1

            # Update the parent, color, and rotate clockwise
            newMinx.parent = currentMinx[1]
            newMinx.color = mp.allFaces[i]
            newMinx.rotateClockwise(newMinx.color)

            # Tell the newMinx to calculate its heuristic
            newMinx.calculateHeuristic()

            # Add to priority queue
            heapq.heappush(priorityQueue, (newMinx.fValue, newMinx))

def main():
    # Reset our HTML File
    # Open our json file and dump it by writing to it!
    with open('components.json', 'w') as f:
        json.dump(mp.componentsListReset, f)

    # Create a root minx
    root = Minx(None, None, 0)
    root.populateNodes()

    # Version Control for Printing Minx
    versionControl = 1

    # Grab the number of random rotations to perform
    while True:
        newInput = input('Please enter a number of random rotations to perform: ')
        try:
            newInput = int(newInput)
            break # Exit, achieved input
        except ValueError:
            # Restart as input was not correct
            print('Please enter a valid number')
    
    # Randomly Rotate the Megaminx
    for _ in range(newInput):
        # Select random face from faceList and rotate it
        randomChoice = random.choice(mp.allFaces)
        print(f'Counter Clockwise Rotating: {randomChoice}')
        root.rotateCounterClockwise(randomChoice)

    # Update the HTML
    root.printMinx(versionControl)

    # Sleep for added effect
    time.sleep(2)

    # Update the heuristic
    root.calculateHeuristic()

    # Inform the solving process will now start
    print('Beginning to Solve')

    # Insanity Check to see we haven't actually solved
    if root.fValue == 0:
        print('Puzzle has already been solved')
        return
    
    # Begin AStar, returns the Minx object with parents leading to correct path
    pathStart, expansionCount = AStar(root)

    print(f'Puzzle has been solved, Depth = {pathStart.depth}, Expanded Nodes = {expansionCount}')

    # Our solutions for Clockwise in Color
    solutionPathColor = []

    # Our solutions for Clockwise in Node
    solutionPathMinx = []

    while pathStart.parent != None:
        solutionPathColor.append(pathStart.color)
        solutionPathMinx.append(pathStart)
        pathStart = pathStart.parent

    # Begin printing our minx
    for i in reversed(solutionPathMinx):
        time.sleep(3)
        print(f'Clockwise Rotating: {i.color}')
        versionControl += 1
        i.printMinx(versionControl)

main()