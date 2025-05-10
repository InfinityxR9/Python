# To sort the given list/array

import numpy as np
import time
import tracemalloc

# === Start tracking ===
start_time = time.perf_counter()
tracemalloc.start()

length = int(input("Enter the array size: "))
low = 1
high = 100000

arr = np.random.randint(low, high + 1, size=length)
print("random array generation successfull")

def Sort(ar):
    arr = ar
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        
            # iteration_number = ((len(arr)-1)*i)-((i*(i+1))/2)+j
            # For total iterations put i=j=n-1 (n == len(arr))
            total_iterations = (len(arr)*((len(arr)-1)))/2
            # print(i,j)
            # print("At the iteration number: ",(i,j), iteration_number)
    
    return [arr, total_iterations]

def isSorted(arr):
    sorting_val = 0

    for i in range(len(arr)):
        if i != len(arr) - 1:
            if arr[i] <= arr[i + 1]: 
                sorting_val += 1

    if sorting_val == len(arr) - 1: 
        return True
    else: 
        return False

if not isSorted(arr):
    sort_call = Sort(arr)
    sorted_arr = sort_call[0]
    total_iterations = sort_call[1]
else: 
    print("Already Sorted array")

# === Stop tracking ===
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(sorted_arr)

# === Report ===
print(f"\n=== Performance Report ===")
print(f"Array Length        : {length}")
print(f"Runtime             : {end_time - start_time:.4f} seconds")
print(f"Current memory      : {current / 10**6:.4f} MB")
print(f"Peak memory         : {peak / 10**6:.4f} MB")
print(f"Total iterations    : {total_iterations}")
