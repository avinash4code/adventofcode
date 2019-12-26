arr = list(map(int,open('./input3.txt','r').read().split(','))) 

# arr = [1,9,10,3,2,3,11,0,99,30,40,50]

arr[1] = 12
arr[2] = 2

print(arr)

for i in range(0, len(arr), 4):
    if (arr[i] == 99):
        break
    if (arr[i] == 1):
        arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]]
    elif (arr[i] == 2):
        arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]]

print(arr)
print(arr[0])
