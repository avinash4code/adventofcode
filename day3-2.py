

def traverse(path):
    wirePositions = {(0,0)}
    curPos = (0,0)
    for loc in path:
        if loc[0] == 'R':
            curPos = moveRight(wirePositions, curPos, int(loc[1:]))
        elif loc[0] == 'L':
            curPos = moveLeft(wirePositions, curPos, int(loc[1:]))
        elif loc[0] == 'U':
            curPos = moveUp(wirePositions, curPos, int(loc[1:]))
        else:
            curPos = moveDown(wirePositions, curPos, int(loc[1:]))
    return wirePositions

def moveRight(wirePositionSet, pos, steps):
    for i in range(1, steps+1):
        wirePositionSet.add((pos[0]+i, pos[1]))
    return (pos[0]+steps, pos[1])

def moveLeft(wirePositionSet, pos, steps):
    for i in range(1, steps+1):
        wirePositionSet.add((pos[0]-i, pos[1]))
    return (pos[0]-steps, pos[1])

def moveUp(wirePositionSet, pos, steps):
    for i in range(1, steps+1):
        wirePositionSet.add((pos[0], pos[1]+i))
    return (pos[0], pos[1]+steps)

def moveDown(wirePositionSet, pos, steps):
    for i in range(1, steps+1):
        wirePositionSet.add((pos[0], pos[1]-i))
    return (pos[0], pos[1]-steps)

def getDistanceFromCenter(loc):
    return abs(loc[0]) + abs(loc[1])

#======================================================================================



# path1 = open('input3-1.txt', 'r').readlines()[0].split(',')
# path2 = open('input3-1.txt', 'r').readlines()[1].split(',')
path1 = 'R8,U5,L5,D3'.split(',')
path2 = 'U7,R6,D4,L4'.split(',')

wire1Positions = {(0,0)}
wire1Steps = {(0,0):0}
wire2Positions = {(0,0)}
wire2Steps = {(0,0):0}
for i in range(0, max(len(path1), len(path2))):
    if i < len(path1):
        moveToLoc(wire1Positions, wire1Steps, path1[i])
    if i < len(path2):
        moveToLoc(wire2Positions, wire2Steps, path2[i])
    
    common = wire1Positions.intersection(wire2Positions)
    common.remove((0,0))
    if len(common) > 0:
        minDistance = findMinDistance(common, wire1Steps, wire2Steps)
        print(minDistance)
        break




# wire1Positions = traverse(path1)
# wire2Positions = traverse(path2)
# common = wire1Positions.intersection(wire2Positions)
# common.remove((0,0))

# minDistance = 99999999999
# for loc in common:
#     minDistance = min(minDistance, getDistanceFromCenter(loc))

# print(minDistance)
