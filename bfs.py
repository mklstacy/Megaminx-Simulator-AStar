'''import megaMap as mp
from collections import deque

starterCorners = mp.starterCorners
starterEdges = mp.starterEdges
Clockwise = mp.adjacentFacesClockwise

cornerStarterGraph = {('White', 'Red', 'Green'): {('White', 'Green', 'Purple'): -1, ('Blue', 'Red', 'White'): -1, ('Red', 'Beige', 'Green'): -1}, ('White', 'Green', 'Purple'): {('White', 'Purple', 'Yellow'): -1, ('Red', 'Green', 'White'): -1, ('Green', 'Cyan', 'Purple'): -1}, ('Blue', 'Red', 'White'): {('Blue', 'White', 'Yellow'): -1, ('Pink', 'Red', 'Blue'): -1, ('Red', 'Green', 'White'): -1}, ('Red', 'Beige', 'Green'): {('Red', 'Green', 'White'): -1, ('Pink', 'Beige', 'Red'): -1, ('Beige', 'Cyan', 'Green'): -1}, ('White', 'Purple', 'Yellow'): {('White', 'Yellow', 'Blue'): -1, ('Green', 'Purple', 'White'): -1, ('Purple', 'Orange', 'Yellow'): -1}, ('Red', 'Green', 'White'): {('Red', 'White', 'Blue'): -1, ('Beige', 'Green', 'Red'): -1, ('Green', 'Purple', 'White'): -1}, ('Green', 'Cyan', 'Purple'): {('Green', 'Purple', 'White'): -1, ('Beige', 'Cyan', 'Green'): -1, ('Cyan', 'Orange', 'Purple'): -1}, ('Blue', 'White', 'Yellow'): {('Blue', 'Yellow', 'Lime'): -1, ('Red', 'White', 'Blue'): -1, ('White', 'Purple', 'Yellow'): -1}, ('Pink', 'Red', 'Blue'): {('Pink', 'Blue', 'Lime'): -1, ('Beige', 'Red', 'Pink'): -1, ('Red', 'White', 'Blue'): -1}, ('Pink', 'Beige', 'Red'): {('Pink', 'Red', 'Blue'): -1, ('Grey', 'Beige', 'Pink'): -1, ('Beige', 'Green', 'Red'): -1}, ('Beige', 'Cyan', 'Green'): {('Beige', 'Green', 'Red'): -1, ('Grey', 'Cyan', 'Beige'): -1, ('Cyan', 'Purple', 'Green'): -1}, ('White', 'Yellow', 'Blue'): {('White', 'Blue', 'Red'): -1, ('Purple', 'Yellow', 'White'): -1, ('Yellow', 'Lime', 'Blue'): -1}, ('Green', 'Purple', 'White'): {('Green', 'White', 'Red'): -1, ('Cyan', 'Purple', 'Green'): -1, ('Purple', 'Yellow', 'White'): -1}, ('Purple', 'Orange', 'Yellow'): {('Purple', 'Yellow', 'White'): -1, ('Cyan', 'Orange', 'Purple'): -1, ('Orange', 'Lime', 'Yellow'): -1}, ('Red', 'White', 'Blue'): {('Red', 'Blue', 'Pink'): -1, ('Green', 'White', 'Red'): -1, ('White', 'Yellow', 'Blue'): -1}, ('Beige', 'Green', 'Red'): {('Beige', 'Red', 'Pink'): -1, ('Cyan', 'Green', 'Beige'): -1, ('Green', 'White', 'Red'): -1}, ('Cyan', 'Orange', 'Purple'): {('Cyan', 'Purple', 'Green'): -1, ('Grey', 'Orange', 'Cyan'): -1, ('Orange', 'Yellow', 'Purple'): -1}, ('Blue', 'Yellow', 'Lime'): {('Blue', 'Lime', 'Pink'): -1, ('White', 'Yellow', 'Blue'): -1, ('Yellow', 'Orange', 'Lime'): -1}, ('Pink', 'Blue', 'Lime'): {('Pink', 'Lime', 'Grey'): -1, ('Red', 'Blue', 'Pink'): -1, ('Blue', 'Yellow', 'Lime'): -1}, ('Beige', 'Red', 'Pink'): {('Beige', 'Pink', 'Grey'): -1, ('Green', 'Red', 'Beige'): -1, ('Red', 'Blue', 'Pink'): -1}, ('Grey', 'Beige', 'Pink'): {('Grey', 'Pink', 'Lime'): -1, ('Cyan', 'Beige', 'Grey'): -1, ('Beige', 'Red', 'Pink'): -1}, ('Grey', 'Cyan', 'Beige'): {('Grey', 'Beige', 'Pink'): -1, ('Orange', 'Cyan', 'Grey'): -1, ('Cyan', 'Green', 'Beige'): -1}, ('Cyan', 'Purple', 'Green'): {('Cyan', 'Green', 'Beige'): -1, ('Orange', 'Purple', 'Cyan'): -1, ('Purple', 'White', 'Green'): -1}, ('White', 'Blue', 'Red'): {('White', 'Red', 'Green'): -1, ('Yellow', 'Blue', 'White'): -1, ('Blue', 'Pink', 'Red'): -1}, ('Purple', 'Yellow', 'White'): {('Purple', 'White', 'Green'): -1, ('Orange', 'Yellow', 'Purple'): -1, ('Yellow', 'Blue', 'White'): -1}, ('Yellow', 'Lime', 'Blue'): {('Yellow', 'Blue', 'White'): -1, ('Orange', 'Lime', 'Yellow'): -1, ('Lime', 'Pink', 'Blue'): -1}, ('Green', 'White', 'Red'): {('Green', 'Red', 'Beige'): -1, ('Purple', 'White', 'Green'): -1, ('White', 'Blue', 'Red'): -1}, ('Orange', 'Lime', 'Yellow'): {('Orange', 'Yellow', 'Purple'): -1, ('Grey', 'Lime', 'Orange'): -1, ('Lime', 'Blue', 'Yellow'): -1}, ('Red', 'Blue', 'Pink'): {('Red', 'Pink', 'Beige'): -1, ('White', 'Blue', 'Red'): -1, ('Blue', 'Lime', 'Pink'): -1}, ('Cyan', 'Green', 'Beige'): {('Cyan', 'Beige', 'Grey'): -1, ('Purple', 'Green', 'Cyan'): -1, ('Green', 'Red', 'Beige'): -1}, ('Grey', 'Orange', 'Cyan'): {('Grey', 'Cyan', 'Beige'): -1, ('Lime', 'Orange', 'Grey'): -1, ('Orange', 'Purple', 'Cyan'): -1}, ('Orange', 'Yellow', 'Purple'): {('Orange', 'Purple', 'Cyan'): -1, ('Lime', 'Yellow', 'Orange'): -1, ('Yellow', 'White', 'Purple'): -1}, ('Blue', 'Lime', 'Pink'): {('Blue', 'Pink', 'Red'): -1, ('Yellow', 'Lime', 'Blue'): -1, ('Lime', 'Grey', 'Pink'): -1}, ('Yellow', 'Orange', 'Lime'): {('Yellow', 'Lime', 'Blue'): -1, ('Purple', 'Orange', 'Yellow'): -1, ('Orange', 'Grey', 'Lime'): -1}, ('Pink', 'Lime', 'Grey'): {('Pink', 'Grey', 'Beige'): -1, ('Blue', 'Lime', 'Pink'): -1, ('Lime', 'Orange', 'Grey'): -1}, ('Beige', 'Pink', 'Grey'): {('Beige', 'Grey', 'Cyan'): -1, ('Red', 'Pink', 'Beige'): -1, ('Pink', 'Lime', 'Grey'): -1}, ('Green', 'Red', 'Beige'): {('Green', 'Beige', 'Cyan'): -1, ('White', 'Red', 'Green'): -1, ('Red', 'Pink', 'Beige'): -1}, ('Grey', 'Pink', 'Lime'): {('Grey', 'Lime', 'Orange'): -1, ('Beige', 'Pink', 'Grey'): -1, ('Pink', 'Blue', 'Lime'): -1}, ('Cyan', 'Beige', 'Grey'): {('Cyan', 'Grey', 'Orange'): -1, ('Green', 'Beige', 'Cyan'): -1, ('Beige', 'Pink', 'Grey'): -1}, ('Orange', 'Cyan', 'Grey'): {('Orange', 'Grey', 'Lime'): -1, ('Purple', 'Cyan', 'Orange'): -1, ('Cyan', 'Beige', 'Grey'): -1}, ('Orange', 'Purple', 'Cyan'): {('Orange', 'Cyan', 'Grey'): -1, ('Yellow', 'Purple', 'Orange'): -1, ('Purple', 'Green', 'Cyan'): -1}, ('Purple', 'White', 'Green'): {('Purple', 'Green', 'Cyan'): -1, ('Yellow', 'White', 'Purple'): -1, ('White', 'Red', 'Green'): -1}, ('Yellow', 'Blue', 'White'): {('Yellow', 'White', 'Purple'): -1, ('Lime', 'Blue', 'Yellow'): -1, ('Blue', 'Red', 'White'): -1}, ('Blue', 'Pink', 'Red'): {('Blue', 'Red', 'White'): -1, ('Lime', 'Pink', 'Blue'): -1, ('Pink', 'Beige', 'Red'): -1}, ('Lime', 'Pink', 'Blue'): {('Lime', 'Blue', 'Yellow'): -1, ('Grey', 'Pink', 'Lime'): -1, ('Pink', 'Red', 'Blue'): -1}, ('Grey', 'Lime', 'Orange'): {('Grey', 'Orange', 'Cyan'): -1, ('Pink', 'Lime', 'Grey'): -1, ('Lime', 'Yellow', 'Orange'): -1}, ('Lime', 'Blue', 'Yellow'): {('Lime', 'Yellow', 'Orange'): -1, ('Pink', 'Blue', 'Lime'): -1, ('Blue', 'White', 'Yellow'): -1}, ('Red', 'Pink', 'Beige'): {('Red', 'Beige', 'Green'): -1, ('Blue', 'Pink', 'Red'): -1, ('Pink', 'Grey', 'Beige'): -1}, ('Purple', 'Green', 'Cyan'): {('Purple', 'Cyan', 'Orange'): -1, ('White', 'Green', 'Purple'): -1, ('Green', 'Beige', 'Cyan'): -1}, ('Lime', 'Orange', 'Grey'): {('Lime', 'Grey', 'Pink'): -1, ('Yellow', 'Orange', 'Lime'): -1, ('Orange', 'Cyan', 'Grey'): -1}, ('Lime', 'Yellow', 'Orange'): {('Lime', 'Orange', 'Grey'): -1, ('Blue', 'Yellow', 'Lime'): -1, ('Yellow', 'Purple', 'Orange'): -1}, ('Yellow', 'White', 'Purple'): {('Yellow', 'Purple', 'Orange'): -1, ('Blue', 'White', 'Yellow'): -1, ('White', 'Green', 'Purple'): -1}, ('Lime', 'Grey', 'Pink'): {('Lime', 'Pink', 'Blue'): -1, ('Orange', 'Grey', 'Lime'): -1, ('Grey', 'Beige', 'Pink'): -1}, ('Orange', 'Grey', 'Lime'): {('Orange', 'Lime', 'Yellow'): -1, ('Cyan', 'Grey', 'Orange'): -1, ('Grey', 'Pink', 'Lime'): -1}, ('Pink', 'Grey', 'Beige'): {('Pink', 'Beige', 'Red'): -1, ('Lime', 'Grey', 'Pink'): -1, ('Grey', 'Cyan', 'Beige'): -1}, ('Beige', 'Grey', 'Cyan'): {('Beige', 'Cyan', 'Green'): -1, ('Pink', 'Grey', 'Beige'): -1, ('Grey', 'Orange', 'Cyan'): -1}, ('Green', 'Beige', 'Cyan'): {('Green', 'Cyan', 'Purple'): -1, ('Red', 'Beige', 'Green'): -1, ('Beige', 'Grey', 'Cyan'): -1}, ('Cyan', 'Grey', 'Orange'): {('Cyan', 'Orange', 'Purple'): -1, ('Beige', 'Grey', 'Cyan'): -1, ('Grey', 'Lime', 'Orange'): -1}, ('Purple', 'Cyan', 'Orange'): {('Purple', 'Orange', 'Yellow'): -1, ('Green', 'Cyan', 'Purple'): -1, ('Cyan', 'Grey', 'Orange'): -1}, ('Yellow', 'Purple', 'Orange'): {('Yellow', 'Orange', 'Lime'): -1, ('White', 'Purple', 'Yellow'): -1, ('Purple', 'Cyan', 'Orange'): -1}}

# adjacentFacesClockwise = {
    # 'White': {
        # 'White': 'White',
        # 'Green': 'Purple', 
        # 'Purple': 'Yellow', 
        # 'Yellow': 'Blue', 
        # 'Blue': 'Red', 
        # 'Red': 'Green',
    # },

# Example of starterCorners
# starterCorners = [
     #('White', 'Red', 'Green'), #0
# ]

megaGraph = {}

def createGraphCorners():
    visited = set()

    queue = deque([('White', 'Red', 'Green')])

    while queue:

        # Grab the first queue
        current = queue.popleft()
        
        # If not already in the main graph, add it
        if not current in megaGraph:
            megaGraph[current] = {}

        # Create the touples for each rotation face
        for rotationFace in range(3):
            firstColor = Clockwise[current[rotationFace]][current[0]]
            secondColor = Clockwise[current[rotationFace]][current[1]]
            thirdColor = Clockwise[current[rotationFace]][current[2]]

            newTuple = (firstColor, secondColor, thirdColor)

            # Check if it is inside the megaGraph
            if not newTuple in megaGraph[current]:
                megaGraph[current][newTuple] = -1

            if not newTuple in visited:
                # Add it to the queue
                queue.append(newTuple)
                visited.add(newTuple)

createGraphCorners()

print(megaGraph)

# Example of starterEdges
# starterEdges = [
    #['White', 'Red'], #0
# ]

graphMapStarter = {}
def createGraphEdges():
    visited = set()

    queue = deque([('White', 'Red')])

    while queue:

        # Grab the first queue
        current = queue.popleft()
        
        # If not already in the main graph, add it
        if not current in megaGraph:
            graphMapStarter[current] = {}

        # Create the touples for each rotation face
        for rotationFace in range(2):
            firstColor = Clockwise[current[rotationFace]][current[0]]
            secondColor = Clockwise[current[rotationFace]][current[1]]

            newTuple = (firstColor, secondColor)

            # Check if it is inside the megaGraph
            if not newTuple in graphMapStarter[current]:
                graphMapStarter[current][newTuple] = -1

            if not newTuple in visited:
                # Add it to the queue
                queue.append(newTuple)
                visited.add(newTuple)

createGraphEdges()
print(graphMapStarter)


graphMapStarter = {('White', 'Red'): {('White', 'Green'): -1, ('Blue', 'Red'): -1}, ('White', 'Green'): {('White', 'Purple'): -1, ('Red', 'Green'): -1}, ('Blue', 'Red'): {('Blue', 'White'): -1, ('Pink', 'Red'): -1}, ('White', 'Purple'): {('White', 'Yellow'): -1, ('Green', 'Purple'): -1}, ('Red', 'Green'): {('Red', 'White'): -1, ('Beige', 'Green'): -1}, ('Blue', 'White'): {('Blue', 'Yellow'): -1, ('Red', 'White'): -1}, ('Pink', 'Red'): {('Pink', 'Blue'): -1, ('Beige', 'Red'): -1}, ('White', 'Yellow'): {('White', 'Blue'): -1, ('Purple', 'Yellow'): -1}, ('Green', 'Purple'): {('Green', 'White'): -1, ('Cyan', 'Purple'): -1}, ('Red', 'White'): {('Red', 'Blue'): -1, ('Green', 'White'): -1}, ('Beige', 'Green'): {('Beige', 'Red'): -1, ('Cyan', 'Green'): -1}, ('Blue', 'Yellow'): {('Blue', 'Lime'): -1, ('White', 'Yellow'): -1}, ('Pink', 'Blue'): {('Pink', 'Lime'): -1, ('Red', 'Blue'): -1}, ('Beige', 'Red'): {('Beige', 'Pink'): -1, ('Green', 'Red'): -1}, ('White', 'Blue'): {('White', 'Red'): -1, ('Yellow', 'Blue'): -1}, ('Purple', 'Yellow'): {('Purple', 'White'): -1, ('Orange', 'Yellow'): -1}, ('Green', 'White'): {('Green', 'Red'): -1, ('Purple', 'White'): -1}, ('Cyan', 'Purple'): {('Cyan', 'Green'): -1, ('Orange', 'Purple'): -1}, ('Red', 'Blue'): {('Red', 'Pink'): -1, ('White', 'Blue'): -1}, ('Cyan', 'Green'): {('Cyan', 'Beige'): -1, ('Purple', 'Green'): -1}, ('Blue', 'Lime'): {('Blue', 'Pink'): -1, ('Yellow', 'Lime'): -1}, ('Pink', 'Lime'): {('Pink', 'Grey'): -1, ('Blue', 'Lime'): -1}, ('Beige', 'Pink'): {('Beige', 'Grey'): -1, ('Red', 'Pink'): -1}, ('Green', 'Red'): {('Green', 'Beige'): -1, ('White', 'Red'): -1}, ('Yellow', 'Blue'): {('Yellow', 'White'): -1, ('Lime', 'Blue'): -1}, ('Purple', 'White'): {('Purple', 'Green'): -1, ('Yellow', 'White'): -1}, ('Orange', 'Yellow'): {('Orange', 'Purple'): -1, ('Lime', 'Yellow'): -1}, ('Orange', 'Purple'): {('Orange', 'Cyan'): -1, ('Yellow', 'Purple'): -1}, ('Red', 'Pink'): {('Red', 'Beige'): -1, ('Blue', 'Pink'): -1}, ('Cyan', 'Beige'): {('Cyan', 'Grey'): -1, ('Green', 'Beige'): -1}, ('Purple', 'Green'): {('Purple', 'Cyan'): -1, ('White', 'Green'): -1}, ('Blue', 'Pink'): {('Blue', 'Red'): -1, ('Lime', 'Pink'): -1}, ('Yellow', 'Lime'): {('Yellow', 'Blue'): -1, ('Orange', 'Lime'): -1}, ('Pink', 'Grey'): {('Pink', 'Beige'): -1, ('Lime', 'Grey'): -1}, ('Beige', 'Grey'): {('Beige', 'Cyan'): -1, ('Pink', 'Grey'): -1}, ('Green', 'Beige'): {('Green', 'Cyan'): -1, ('Red', 'Beige'): -1}, ('Yellow', 'White'): {('Yellow', 'Purple'): -1, ('Blue', 'White'): -1}, ('Lime', 'Blue'): {('Lime', 'Yellow'): -1, ('Pink', 'Blue'): -1}, ('Lime', 'Yellow'): {('Lime', 'Orange'): -1, ('Blue', 'Yellow'): -1}, ('Orange', 'Cyan'): {('Orange', 'Grey'): -1, ('Purple', 'Cyan'): -1}, ('Yellow', 'Purple'): {('Yellow', 'Orange'): -1, ('White', 'Purple'): -1}, ('Red', 'Beige'): {('Red', 'Green'): -1, ('Pink', 'Beige'): -1}, ('Cyan', 'Grey'): {('Cyan', 'Orange'): -1, ('Beige', 'Grey'): -1}, ('Purple', 'Cyan'): {('Purple', 'Orange'): -1, ('Green', 'Cyan'): -1}, ('Lime', 'Pink'): {('Lime', 'Blue'): -1, ('Grey', 'Pink'): -1}, ('Orange', 'Lime'): {('Orange', 'Yellow'): -1, ('Grey', 'Lime'): -1}, ('Pink', 'Beige'): {('Pink', 'Red'): -1, ('Grey', 'Beige'): -1}, ('Lime', 'Grey'): {('Lime', 'Pink'): -1, ('Orange', 'Grey'): -1}, ('Beige', 'Cyan'): {('Beige', 'Green'): -1, ('Grey', 'Cyan'): -1}, ('Green', 'Cyan'): {('Green', 'Purple'): -1, ('Beige', 'Cyan'): -1}, ('Lime', 'Orange'): {('Lime', 'Grey'): -1, ('Yellow', 'Orange'): -1}, ('Orange', 'Grey'): {('Orange', 'Lime'): -1, ('Cyan', 'Grey'): -1}, ('Yellow', 'Orange'): {('Yellow', 'Lime'): -1, ('Purple', 'Orange'): -1}, ('Cyan', 'Orange'): {('Cyan', 'Purple'): -1, ('Grey', 'Orange'): -1}, ('Purple', 'Orange'): {('Purple', 'Yellow'): -1, ('Cyan', 'Orange'): -1}, ('Grey', 'Pink'): {('Grey', 'Lime'): -1, ('Beige', 'Pink'): -1}, ('Grey', 'Lime'): {('Grey', 'Orange'): -1, ('Pink', 'Lime'): -1}, ('Grey', 'Beige'): {('Grey', 'Pink'): -1, ('Cyan', 'Beige'): -1}, ('Grey', 'Cyan'): {('Grey', 'Beige'): -1, ('Orange', 'Cyan'): -1}, ('Grey', 'Orange'): {('Grey', 'Cyan'): -1, ('Lime', 'Orange'): -1}}

def runBFS(source_tuple):
    # Create a visited set and distance dictionary
    visited = set()
    distance = {source_tuple: 0}

    # Create a queue and enqueue the source tuple
    queue = deque([source_tuple])

    while queue:
        # Dequeue the first tuple from the queue
        current = queue.popleft()

        # Update the visited set
        visited.add(current)

        # Enqueue all unvisited neighbors and update their distances
        for neighbor, _ in graphMapStarter[current].items():
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                distance[neighbor] = distance[current] + 1

    return distance


# Begin the ultimate megaGraph of a Megaminx
megaGraph = {}

# Runs our BFS Algorithm to calculate the distance from every single possible orientation in the megaminx
for index, _ in graphMapStarter.items():
    megaGraph[index] = runBFS(index)

TempValue = 0
for index, value in megaGraph.items():
    TempValue += 1
    for cool in value:
        TempValue += 1
'''

        