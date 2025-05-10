import time
import tracemalloc
import random

# === Start tracking ===
start_time = time.perf_counter()
tracemalloc.start()

length = int(input("Enter the array size: "))
low = 1
high = 100000


numList = [random.randint(low, high) for _ in range(length)]
print("random array generation successfull")

sortedlist = []

def minima(myList):
    assumedMin = myList[0] # lets assume the first one is minimum

    for i in myList:
        if assumedMin > i: assumedMin = i
        else: continue

    return assumedMin
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

def sort(argList):
    if len(argList) != 0:
        sortedlist.append(minima(argList))
        argList.remove(minima(argList))

        if len(argList) != 0:
            sort(argList)

        else:
            return sortedlist

if not isSorted(numList): 
    sort(numList)

else: print("The list is already sorted")

# === Stop tracking ===
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print('the sorted list is: ', sortedlist)

# === Report ===
print(f"\n=== Performance Report ===")
print(f"Array Length        : {length}")
print(f"Runtime             : {end_time - start_time:.4f} seconds")
print(f"Current memory      : {current / 10**6:.4f} MB")
print(f"Peak memory         : {peak / 10**6:.4f} MB")
# print(f"Total iterations    : {total_iterations}")

