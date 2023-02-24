# time complexity O(log n)
arr = [1,2,3,4,5,6,7,8,9]

def binarySearch (item, arr):
    left = 0
    right = len(arr) - 1
    while right >= left:
        mid = (left + right) // 2
        if arr[mid] == item:
            return mid
        else:
            if arr[mid] < item:
                left = mid + 1
            else:
                right = mid - 1

print(binarySearch(9, arr))