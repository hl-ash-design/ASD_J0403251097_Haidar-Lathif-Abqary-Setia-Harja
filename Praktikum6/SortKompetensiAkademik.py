data = [43,76,12,89,33,57,98,22,68,9]

def bubbleSort(data):
    for reps in range(len(data)-1,0,-1):
        for i in range(reps):
            if data[i] < data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
    return data[:5]

print(bubbleSort(data))