# To sort the given list/array

"""

arr = [5, 2, 9, 1, 5, 6]
sorted = []
i = 5
i<j
"""

arr = [1, 2, 5, 5, 6, 9]

def Sort(ar):
    arr = ar
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr

def isSorted(arr):
    sorting_val = 0

    for i in range(len(arr)):
        if i!=len(arr)-1:
            if arr[i] <= arr[i+1]: sorting_val+=1

    if sorting_val == len(arr)-1: return True
    else: return False

if not isSorted(arr): print(Sort(arr))
else: print("Already Sorted array")
