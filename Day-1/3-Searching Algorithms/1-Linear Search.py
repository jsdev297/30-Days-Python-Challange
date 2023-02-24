arr = [1,2,3,4,5,6,7,8,9]

def linearSearch (item, arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == item:
            return i
    return -1
    
print(linearSearch(12,arr))

# time complexity O(n)