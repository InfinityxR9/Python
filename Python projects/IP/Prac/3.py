# Operations on Pandas Dataframe
import pandas as pd
import numpy as np

dataDic = {
    'Arnab': [90, 91, 97],
    'Ramit': [92, 81, 96],
    'Samridhi': [81, 71, 67],
    'Riya': [81, 71, 67],
    'Mallika': [94, 95, 99],
    'Preeti': [89, 78, 76]
}

data = pd.DataFrame(dataDic, index=['Maths', 'Science', 'Hindi'])

data['Aryan'] = [99, 98, 100]

data.loc['IP'] = [95, 84, 60, 96, 87, 70, 99]

# data[:] = 0
# data = data.rename({'Arnab': 'Adithya'}, axis='columns')
data = data.rename({'Arnab': 'Adithya'}, axis=1)

data.loc[:, 'Pranjal'] = [91, 92, 97, 98]

# print(data.loc['Maths':'Hindi','Adithya'])

# print(data.loc[['Science', 'Hindi']])

# print(data)

