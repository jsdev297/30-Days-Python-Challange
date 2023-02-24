arr = [1,5,2,10,3,4]

def selectionSort (arr):
    length = len(arr)
    for i in range(length):
        minIndex = i
        for j in range(i+1, length):
            if arr[minIndex] > arr[j]:
                minIndex = j
        if minIndex is not i:
            temp = arr[minIndex]
            arr[minIndex] = arr[i]
            arr[i] = temp
    print(arr)

selectionSort(arr)