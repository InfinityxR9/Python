import pandas as pd

db = {
    "Name": ["Aryan", "kanha", "Adithya", "Pranjal"],
    "Alias": ["Infinity", "Gadha","GC", "Jala"],
    "Class": [12, 7, 12, 12],
    "Marks in Maths": [101, 69, 96, 99],
    "Status": ["Pass", "Fail", "Pass", "Pass"]
}

data = pd.DataFrame(db)
data.index += 1

print(data["Name"])
print(data.loc[[1,2],"Name"])

print(data)

# To remove the last row
# print(data.drop(4, axis='rows'))

# or
siz = data.shape[0]
data = data.loc[data.index[0]:siz-1]

print(data)

