numbers = [5, 6, 9, 2, 7, 1, 4, 2, 8, 3]
print("Normal array")
print(numbers)
print("\n")

def bubbleSort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] =  array[j+1], array[j]
    return array


def selectionSort(array):
    hold = None
    for i in range(len(array)):
            minor_Number_index = i
            for j in range(i+1, len(array)):
                if array[minor_Number_index] > array[j]:
                    minor_Number_index = j
            hold = array[i]
            array[i] = array[minor_Number_index]
            array[minor_Number_index] = hold
    return array


def insertionSort(array):
    for i in range(1, len(array)):
        value=array[i]
        position=i
        while position > 0 and array[position-1] > value:
            array[position]=array[position-1]
            position=position-1
        array[position]=value
    return array


# Test
numbers= bubbleSort(numbers)
# Print
print("Sorted array")
print(numbers)
