import sys
numbers = [5, 6, 9, 2, 7, 1, 4, 2, 8, 3]
print("Normal array")
for a in numbers:
    print(a, end=",")
print("\n")


def selectionSort(array):
    for i in range(len(array)): 
        min_idx = i 
        for j in range(i+1, len(array)): 
            if array[min_idx] > array[j]: 
                min_idx = j        
        array[i], array[min_idx] = array[min_idx], array[i] 
    return array


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


#Test
numbers = selectionSort(numbers)
#Print
print ("Sorted array") 
for i in range(len(numbers)): 
    print(numbers[i], end=",")