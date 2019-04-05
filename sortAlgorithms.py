test = [5, 6, 9, 2, 7, 1, 4, 2, 8, 3]
for a in test:
    print(a, end=",")
print("")


def insertionSort(array):
    hold = None
    index = 0
    for x in array:
        index = array.index(x)
        hold = x
        for a in range(index-1, -1, -1):
            index = index-1
            if hold < array[index]:
                array[index+1] = array[index]
                try:
                    array[index] = array[index-1]
                except:
                    pass
            else:
                array[index] = hold
    return array




test = insertionSort(test)
for a in test:
    print(a, end=",")
