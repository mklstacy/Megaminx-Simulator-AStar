
# You will need this to pack the information into the components.json file
import json, time
import megaMap as mp

# The printing characterization
upwardPrint = mp.megaPrintUpward
downwardPrint = mp.megaPrintDownward

# Used for printing purposes
class Face:
    def __init__(self, color, direction):
        # Color of the face
        self.color = color

        # Direction of the face (Up or Down)
        self.direction = direction

        # Every component of the face is a color
        self.components = {
            0: color,
            1: color,
            2: color,
            3: color,
            4: color,
            5: color,
            6: color,
            7: color,
            8: color,
            9: color,
        }

    # Grabs the color of each node on the face
    def updateColor(self, cornerList, edgeList):
        
        # Loop through the corner list and edge list
        if self.direction == 'Up':
            for index, tempEdge in enumerate(upwardPrint[self.color]):
                # Determine if Corner or Edge
                if index % 2 == 0:
                    # Update
                    self.components[index] = cornerList[upwardPrint[self.color][index]].grabColor(self.color)
                else:
                    # Update
                    self.components[index] = edgeList[upwardPrint[self.color][index]].grabColor(self.color)
        elif self.direction == 'Down':
            for index, tempEdge in enumerate(downwardPrint[self.color]):
                # Determine if Corner or Edge
                if index % 2 == 0:
                    # Update
                    self.components[index] = cornerList[downwardPrint[self.color][index]].grabColor(self.color)
                else:
                    # Update
                    self.components[index] = edgeList[downwardPrint[self.color][index]].grabColor(self.color)