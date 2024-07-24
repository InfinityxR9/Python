# Pandas dataframe

import pandas as pd
import numpy as np

# df = pd.DataFrame([[10, 20, 30], [40, 50, 60]], index=['a', 'b'], columns=['C1', 'C2', 'C3'])

dic = {
    '10To30': [10, 20, 30],
    '40To60': [40, 50, 60]
}

# df = pd.DataFrame(dic, index=['i1', 'i2', 'i3'])

lisDic = [
    {
        '10To30': [10,20,30],
        '40To60': [40, 50, 60]
    },
    {
        '10To30': 10,
        '40To60': 40
    },
    {
        '10To30': 20,
        '40To60': 50
    },
    {
        '10To30': 30,
        '40To60': 60
    },
]
df = pd.DataFrame(lisDic, index=['i1', 'i2', 'i3', 'i4'])

print(df)
