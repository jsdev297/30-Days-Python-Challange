myArr = [9, 4, 8, 6, 3, 7, 1]

def insertion_sort (arr):
    length = len(arr)
    for i in range(1, length):
        t = arr[i]
        j = i - 1
        while j >= 0 and t < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = t
    return arr

print(insertion_sort(myArr))