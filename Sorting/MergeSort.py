# Selection 
def selectionSort(arr):
    n= len(arr)
    for i in range (n-1):
        min_index = i
        for j in range (i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j 
            arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr


def bubbleSort(arr):
    n = len(arr)
    for i in range (n-1):
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def insertionSort(arr):
    n = len(arr)
    for i in range (1,n):
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
# print 
print(selectionSort([13,46,24,52,20,9]))
print(bubbleSort([13,46,24,52,20,9]))
print(insertionSort([13,46,24,52,20,9]))