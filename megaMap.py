# The adjacent Clockwise mapping of the faces
adjacentFacesClockwise = {
    'White': {
        'White': 'White',
        'Green': 'Purple', 
        'Purple': 'Yellow', 
        'Yellow': 'Blue', 
        'Blue': 'Red', 
        'Red': 'Green',
    },
    'Green': {
        'Green': 'Green',
        'Purple': 'White',
        'White': 'Red',
        'Red': 'Beige',
        'Beige': 'Cyan',
        'Cyan': 'Purple'
    },
    'Purple': {
        'Purple': 'Purple',
        'Cyan': 'Orange',
        'Orange': 'Yellow',
        'Yellow': 'White',
        'White': 'Green',
        'Green': 'Cyan',
    },
    'Red': {
        'Red': 'Red',
        'Blue': 'Pink',
        'Pink': 'Beige',
        'Beige': 'Green',
        'Green': 'White',
        'White': 'Blue'
    },
    'Blue': {
        'Blue': 'Blue',
        'Yellow': 'Lime',
        'Lime': 'Pink',
        'Pink': 'Red',
        'Red': 'White',
        'White': 'Yellow'
    },
    'Yellow': {
        'Yellow': 'Yellow',
        'Orange': 'Lime',
        'Lime': 'Blue',
        'Blue': 'White',
        'White': 'Purple',
        'Purple': 'Orange'
    },
    'Grey': {
        'Grey': 'Grey',
        'Orange': 'Cyan',
        'Cyan': 'Beige',
        'Beige': 'Pink',
        'Pink': 'Lime',
        'Lime': 'Orange'
    },
    'Beige': {
        'Beige': 'Beige',
        'Red': 'Pink',
        'Pink': 'Grey',
        'Grey': 'Cyan',
        'Cyan': 'Green',
        'Green': 'Red'
    },
    'Pink': {
        'Pink': 'Pink',
        'Red': 'Blue',
        'Blue': 'Lime',
        'Lime': 'Grey',
        'Grey': 'Beige',
        'Beige': 'Red'
    },
    'Lime': {
        'Lime': 'Lime',
        'Blue': 'Yellow',
        'Yellow': 'Orange',
        'Orange': 'Grey',
        'Grey': 'Pink',
        'Pink': 'Blue'
    },
    'Orange': {
        'Orange': 'Orange',
        'Lime': 'Yellow',
        'Yellow': 'Purple',
        'Purple': 'Cyan',
        'Cyan': 'Grey',
        'Grey': 'Lime'
    },
    'Cyan': {
        'Cyan': 'Cyan',
        'Purple': 'Green',
        'Green': 'Beige',
        'Beige': 'Grey',
        'Grey': 'Orange',
        'Orange': 'Purple',
    },
}
# The adjacent Counter-Clockwise mapping of the faces
adjacentFacesCounterClockwise = {
    'White': {
        'White': 'White',
        'Green': 'Red',
        'Red': 'Blue',
        'Blue': 'Yellow',
        'Yellow': 'Purple',
        'Purple': 'Green',
    },
    'Green': {
        'Green': 'Green',
        'Purple': 'Cyan',
        'Cyan': 'Beige',
        'Beige': 'Red',
        'Red': 'White',
        'White': 'Purple'
    },
    'Purple': {
        'Purple': 'Purple',
        'Cyan': 'Green',
        'Green': 'White',
        'White': 'Yellow',
        'Yellow': 'Orange',
        'Orange': 'Cyan',
    },
    'Red': {
        'Red': 'Red',
        'Blue': 'White',
        'White': 'Green',
        'Green': 'Beige',
        'Beige': 'Pink',
        'Pink': 'Blue',
    },
    'Blue': {
        'Blue': 'Blue',
        'Yellow': 'White',
        'White': 'Red',
        'Red': 'Pink',
        'Pink': 'Lime',
        'Lime': 'Yellow'
    },
    'Yellow': {
        'Yellow': 'Yellow',
        'Orange': 'Purple',
        'Purple': 'White',
        'White': 'Blue',
        'Blue': 'Lime',
        'Lime': 'Orange'
    },
    'Grey': {
        'Grey': 'Grey',
        'Orange': 'Lime',
        'Lime': 'Pink',
        'Pink': 'Beige',
        'Beige': 'Cyan',
        'Cyan': 'Orange'
    },
    'Beige': {
        'Beige': 'Beige',
        'Red': 'Green',
        'Green': 'Cyan',
        'Cyan': 'Grey',
        'Grey': 'Pink',
        'Pink': 'Red',
    },
    'Pink': {
        'Pink': 'Pink',
        'Red': 'Beige',
        'Beige': 'Grey',
        'Grey': 'Lime',
        'Lime': 'Blue',
        'Blue': 'Red'
    },
    'Lime': {
        'Lime': 'Lime',
        'Blue': 'Pink',
        'Pink': 'Grey',
        'Grey': 'Orange',
        'Orange': 'Yellow',
        'Yellow': 'Blue'
    },
    'Orange': {
        'Orange': 'Orange',
        'Lime': 'Grey',
        'Grey': 'Cyan',
        'Cyan': 'Purple',
        'Purple': 'Yellow',
        'Yellow': 'Lime'
    },
    'Cyan': {
        'Cyan': 'Cyan',
        'Purple': 'Orange',
        'Orange': 'Grey',
        'Grey': 'Beige',
        'Beige': 'Green',
        'Green': 'Purple',
    },
}

starterCorners = [
    ['White', 'Red', 'Green'], #0
    ['White', 'Green', 'Purple'], #1
    ['White', 'Purple', 'Yellow'], #2
    ['White', 'Yellow', 'Blue'], #3
    ['White', 'Blue', 'Red'], #4
    ['Grey', 'Orange', 'Cyan'], #5
    ['Grey', 'Cyan', 'Beige'], #6
    ['Grey', 'Beige', 'Pink'], #7
    ['Grey', 'Pink', 'Lime'], #8
    ['Grey', 'Lime', 'Orange'], #9
    ['Purple', 'Cyan', 'Orange'], #10
    ['Purple', 'Orange', 'Yellow'], #11
    ['Purple', 'Green', 'Cyan'], #12
    ['Green', 'Beige', 'Cyan'], #13
    ['Green', 'Red', 'Beige'], #14
    ['Red', 'Pink', 'Beige'], #15
    ['Pink', 'Red', 'Blue'], #16
    ['Lime', 'Pink', 'Blue'], #17
    ['Blue', 'Yellow', 'Lime'], #18
    ['Yellow', 'Orange', 'Lime'], #19
]

starterEdges = [
    ['White', 'Red'], #0
    ['White', 'Green'], #1
    ['White', 'Purple'], #2
    ['White', 'Yellow'], #3
    ['White', 'Blue'], #4
    ['Grey', 'Orange'], #5
    ['Grey', 'Cyan'], #6
    ['Grey', 'Beige'], #7
    ['Grey', 'Pink'], #8
    ['Grey', 'Lime'], #9
    ['Purple', 'Orange'], #10
    ['Purple', 'Yellow'], #11
    ['Yellow', 'Orange'], #12
    ['Purple', 'Cyan'], #13
    ['Orange', 'Cyan'], #14
    ['Orange', 'Lime'], #15
    ['Lime', 'Pink'], #16
    ['Pink', 'Beige'], #17
    ['Cyan', 'Beige'], #18
    ['Green', 'Red'], #19
    ['Green', 'Purple'], #20
    ['Red', 'Blue'], #21
    ['Blue', 'Yellow'], #22
    ['Yellow', 'Lime'], #23
    ['Blue', 'Lime'], #24
    ['Pink', 'Blue'], #25
    ['Pink', 'Red'], #26
    ['Beige', 'Red'], #27
    ['Green', 'Beige'], #28
    ['Cyan', 'Green'], #29
]

minxEdges = {
    'White' : [0, 1, 2, 3, 4],
    'Red': [19, 0, 21, 26, 27],
    'Green': [28, 29, 20, 1, 19],
    'Purple': [20, 13, 10, 11, 2],
    'Yellow': [3, 11, 12, 23, 22],
    'Blue' : [22, 24, 25, 21, 4],
    'Grey': [6, 7, 8, 9, 5],
    'Orange': [14, 5, 15, 12, 10],
    'Cyan': [6, 14, 13, 29, 18],
    'Beige': [17, 7, 18, 28, 27],
    'Pink': [26, 25, 16, 8, 17],
    'Lime': [16, 24, 23, 15, 9],
}

minxCorners = {
    'White' : [0,1,2,3,4],
    'Red': [0,4,16,15,14],
    'Green': [0,14,13,12,1],
    'Purple': [1,12,10,11,2],
    'Yellow': [2,11,19,18,3],
    'Blue' : [3,18,17,16,4],
    'Grey': [5,6,7,8,9],
    'Orange': [10,5,9,19,11],
    'Cyan': [12,13,6,5,10],
    'Beige': [13,14,15,7,6],
    'Pink': [7,15,16,17,8],
    'Lime': [8,17,18,19,9],
}

# For printing the Upward Pentagons
megaPrintUpward = {
    'Red': [16, 26, 15, 27, 14, 19, 0, 0, 4, 21],
    'Green': [0, 19, 14, 28, 13, 29, 12, 20, 1, 1],
    'Purple': [2, 2, 1, 20, 12, 13, 10, 10, 11, 11],
    'Yellow': [18, 22, 3, 3, 2, 11, 11, 12, 19, 23],
    'Blue': [17, 25, 16, 21, 4, 4, 3, 22, 18, 24],
    'Grey': [9, 5, 5, 6, 6, 7, 7, 8, 8, 9],
}

# For printing the Downward Pentagons
megaPrintDownward = {
    'Orange': [5, 5, 9, 15, 19, 12, 11, 10, 10, 14],
    'Cyan': [13, 18, 6, 6, 5, 14, 10, 13, 12, 29],
    'Beige': [14, 27, 15, 17, 7, 7, 6, 18, 13, 28],
    'Pink': [15, 26, 16, 25, 17, 16, 8, 8, 7, 17],
    'Lime': [8, 16, 17, 24, 18, 23, 19, 15, 9, 9],
    'White': [1, 2, 2, 3, 3, 4, 4, 0, 0, 1],
}

allFaces = [
    'White',
    'Red',
    'Green',
    'Purple',
    'Yellow',
    'Blue',
    'Grey',
    'Orange',
    'Cyan',
    'Beige',
    'Pink',
    'Lime',
]

# An example of how to map the components to their corresponding elements
componentsListReset = {
    'Version' : 0,
    'Colors' : {
        'Red' : {
        '0' : 'Red',
        '1' : 'Red',
        '2' : 'Red',
        '3' : 'Red',
        '4' : 'Red',
        '5' : 'Red',
        '6' : 'Red',
        '7' : 'Red',
        '8' : 'Red',
        '9' : 'Red',
        },
        'Green' : {
        '0' : 'Green',
        '1' : 'Green',
        '2' : 'Green',
        '3' : 'Green',
        '4' : 'Green',
        '5' : 'Green',
        '6' : 'Green',
        '7' : 'Green',
        '8' : 'Green',
        '9' : 'Green',
        },
        'Purple' : {
        '0' : 'Purple',
        '1' : 'Purple',
        '2' : 'Purple',
        '3' : 'Purple',
        '4' : 'Purple',
        '5' : 'Purple',
        '6' : 'Purple',
        '7' : 'Purple',
        '8' : 'Purple',
        '9' : 'Purple',
        },
        'Yellow' : {
        '0' : 'Yellow',
        '1' : 'Yellow',
        '2' : 'Yellow',
        '3' : 'Yellow',
        '4' : 'Yellow',
        '5' : 'Yellow',
        '6' : 'Yellow',
        '7' : 'Yellow',
        '8' : 'Yellow',
        '9' : 'Yellow',
        },
        'Blue' : {
        '0' : 'Blue',
        '1' : 'Blue',
        '2' : 'Blue',
        '3' : 'Blue',
        '4' : 'Blue',
        '5' : 'Blue',
        '6' : 'Blue',
        '7' : 'Blue',
        '8' : 'Blue',
        '9' : 'Blue',
        },
        'Grey' : {
        '0' : 'Grey',
        '1' : 'Grey',
        '2' : 'Grey',
        '3' : 'Grey',
        '4' : 'Grey',
        '5' : 'Grey',
        '6' : 'Grey',
        '7' : 'Grey',
        '8' : 'Grey',
        '9' : 'Grey',
        },
        'White' : {
        '0' : 'White',
        '1' : 'White',
        '2' : 'White',
        '3' : 'White',
        '4' : 'White',
        '5' : 'White',
        '6' : 'White',
        '7' : 'White',
        '8' : 'White',
        '9' : 'White',
        },
        'Orange' : {
        '0' : 'Orange',
        '1' : 'Orange',
        '2' : 'Orange',
        '3' : 'Orange',
        '4' : 'Orange',
        '5' : 'Orange',
        '6' : 'Orange',
        '7' : 'Orange',
        '8' : 'Orange',
        '9' : 'Orange',
        },
        'Cyan' : {
        '0' : 'Cyan',
        '1' : 'Cyan',
        '2' : 'Cyan',
        '3' : 'Cyan',
        '4' : 'Cyan',
        '5' : 'Cyan',
        '6' : 'Cyan',
        '7' : 'Cyan',
        '8' : 'Cyan',
        '9' : 'Cyan',
        },
        'Beige' : {
        '0' : 'Beige',
        '1' : 'Beige',
        '2' : 'Beige',
        '3' : 'Beige',
        '4' : 'Beige',
        '5' : 'Beige',
        '6' : 'Beige',
        '7' : 'Beige',
        '8' : 'Beige',
        '9' : 'Beige',
        },
        'Pink' : {
        '0' : 'Pink',
        '1' : 'Pink',
        '2' : 'Pink',
        '3' : 'Pink',
        '4' : 'Pink',
        '5' : 'Pink',
        '6' : 'Pink',
        '7' : 'Pink',
        '8' : 'Pink',
        '9' : 'Pink',
        },
        'Lime' : {
        '0' : 'Lime',
        '1' : 'Lime',
        '2' : 'Lime',
        '3' : 'Lime',
        '4' : 'Lime',
        '5' : 'Lime',
        '6' : 'Lime',
        '7' : 'Lime',
        '8' : 'Lime',
        '9' : 'Lime',
        },
    }
}

# Checks if the Clockwise and Counter-Clockwise Dictionaries are opposites
def sanityCheckFaces():
    for face, value in adjacentFacesClockwise.items():
        for key, part in value.items():
            if adjacentFacesCounterClockwise[face][part] == key:
                print(f'The {face} matches opposite')
            else:
                print(f'Error on {face}')

# Checks if the Clockwise starterCorners are a match for correct orientation
def sanityCheckCorner():
    for i in starterCorners:
        if adjacentFacesClockwise[i[0]][i[1]] == i[2]:
            print(f'The {i} matches sanity check')
        else:
            print(f'Error on index {i}')