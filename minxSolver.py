import random, time, heapq, copy, json
import megaMap as mp
from Minx import Minx

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
    time.sleep(1)

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
        # Sleep for more added effect
        time.sleep(2)
        
        # Print the solution
        print(f'Clockwise Rotating: {i.color}')

        # Update our HTML
        versionControl += 1
        i.printMinx(versionControl)

main()