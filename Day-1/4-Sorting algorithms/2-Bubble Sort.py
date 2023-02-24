
def bubbleSort (arr):
    length = len(arr)
    for i in range(length):
        for j in range(0, length-1-i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print(arr)

bubbleSort([1,5,9,10,8,4])