# Pandas series
import pandas as pd
import numpy as np

arr = np.array([1,2])

# series = pd.Series(arr, index=['a1', 'a2'])
dic = {
    'Name': 'Aryan Sisodiya',
    'Class': 12,
    'Section': 'S1'
}

# series = pd.Series(dic, index=[10,20,30])
# series = pd.Series(dic)

series = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
series.name = 'The Series'
series.index.name = 'The indices'

print(series)
# print(series[::-1])
print(series.index)
print(series)

# print(series.iloc['b'])
