def selectionSort(data):
    for fullslot in range(len(data)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fullslot+1):
            if data[location]>data[positionOfMax]:
                positionOfMax = location
        
        #Swap
        temp = data[fullslot]
        data[fullslot] = data[positionOfMax]
        data[positionOfMax] = temp

data = [54,26,93,17,77,31,44,55,20]
selectionSort(data)
print(data)