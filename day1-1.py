import math

def GetFuel(mass):
    return math.floor(mass / 3) - 2

totalFuel = 0
for line in open('./input1.txt', 'r').readlines():
    totalFuel += GetFuel(int(line))
    # print(line)
  
print (int(totalFuel))
