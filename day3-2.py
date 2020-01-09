
class Wire(object):
    def __init__(self):
        self.curLoc = (0,0)
        self.positions = {self.curLoc}
        self.locationSteps = {}
        self.curStepCount = 0


def moveToLoc(wire, loc):
    if loc[0] == 'R':        
        goRight(wire, int(loc[1:]))
    elif loc[0] == 'L':
        goLeft(wire, int(loc[1:]))
    elif loc[0] == 'U':
        goUp(wire, int(loc[1:]))
    else:
        goDown(wire, int(loc[1:]))

def goRight(wire, stepCount):
    for i in range(1, stepCount+1):
        newPos = (wire.curLoc[0]+i, wire.curLoc[1])
        wire.positions.add(newPos)
        wire.curStepCount += 1
        wire.locationSteps[newPos] = wire.curStepCount
    wire.curLoc = (wire.curLoc[0]+stepCount, wire.curLoc[1])

def goLeft(wire, stepCount):
    for i in range(1, stepCount+1):
        newPos = (wire.curLoc[0]-i, wire.curLoc[1])
        wire.positions.add(newPos)
        wire.curStepCount += 1
        wire.locationSteps[newPos] = wire.curStepCount
    wire.curLoc = (wire.curLoc[0]-stepCount, wire.curLoc[1])

def goUp(wire, stepCount):
    for i in range(1, stepCount+1):
        newPos = (wire.curLoc[0], wire.curLoc[1]+i)
        wire.positions.add(newPos)
        wire.curStepCount += 1
        wire.locationSteps[newPos] = wire.curStepCount
    wire.curLoc = (wire.curLoc[0], wire.curLoc[1]+stepCount)

def goDown(wire, stepCount):
    for i in range(1, stepCount+1):
        newPos = (wire.curLoc[0], wire.curLoc[1]-i)
        wire.positions.add(newPos)
        wire.curStepCount += 1
        wire.locationSteps[newPos] = wire.curStepCount
    wire.curLoc = (wire.curLoc[0], wire.curLoc[1]-stepCount)

def findMinStepLoc(wire1, wire2, common):
    minDistance = 9999999999
    for loc in common:
        minDistance = min(wire1.locationSteps[loc] + wire2.locationSteps[loc], minDistance)
    return minDistance

path1 = open('input5.txt', 'r').readlines()[0].split(',')
path2 = open('input5.txt', 'r').readlines()[1].split(',')
# # path1 = 'R8,U5,L5,D3'.split(',')
# # path2 = 'U7,R6,D4,L4'.split(',')

wire1 = Wire()
wire2 = Wire()

for i in range(0, max(len(path1), len(path2))):
    if i < len(path1):
        moveToLoc(wire1, path1[i])
    if i < len(path2):
        moveToLoc(wire2, path2[i])
    
    common = wire1.positions.intersection(wire2.positions)
    # print (common)
    common.remove((0,0))
    if len(common) > 0:
        minDistance = findMinStepLoc(wire1, wire2, common)
        print(minDistance)
        break


##### ANS = 15678