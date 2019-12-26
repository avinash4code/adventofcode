
def ProcessIntCode(arr, noun, verb):
    arr[1] = noun
    arr[2] = verb
    for i in range(0, len(arr), 4):
        if (arr[i] == 99):
            break
        if (arr[i] == 1 and arr[i+3]<len(arr)):
            arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]]
        elif (arr[i] == 2 and arr[i+3]<len(arr)):
            arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]]

    return arr[0]


for i in range(0,100):
    for j in range(0,100):
        arr = list(map(int,open('./input3.txt','r').read().split(','))) 
        if (ProcessIntCode(arr,i,j) == 19690720):
            print(i,j)
            exit()

