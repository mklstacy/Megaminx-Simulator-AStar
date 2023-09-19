import json
import megaMap as mp
from Node import Node
from Face import Face

# The printing characterization
upwardPrint = mp.megaPrintUpward
downwardPrint = mp.megaPrintDownward

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