import math

def GetFuel(mass):
    fuel = totalFuel = math.floor(mass / 3) - 2
    while fuel > 0:
        fuel = math.floor(fuel / 3) - 2
        if fuel>0:
            totalFuel += fuel
    return totalFuel

# def GetRealFuel(mass):
#     return math.floor(mass / 3) - 2

# print(GetFuel(14))
# print(int(GetFuel(1969)))
# print(GetFuel(100756))

totalFuel = 0
for line in open('./input1.txt', 'r').readlines():
    totalFuel += GetFuel(int(line))

print (int(totalFuel))
