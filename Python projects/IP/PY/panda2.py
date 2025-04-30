import pandas as pd

dataDict1 = {
    "col1": pd.Series([1,2,3], index=['a', 'b', 'c']),
    "col2": pd.Series([0, 78, -25, 13], index=['a', 'b', 'c', 'd'])
}

df1 = pd.DataFrame(dataDict1)

# print(df1)
# print(df1.loc[::-2, ::-1])

df2 = pd.DataFrame([[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15]])
# print(df2)

dataDict2 = {
    "Populations":[64654968, 654564, 1349564, 16541, 21345],
    "Hospitals": [558, 3498, 489, 658, 358],
    "Schools": [9868, 5487, 8928, 1868, 6578]
}

df3 = pd.DataFrame(dataDict2, index=["Delhi", "Kolkata", "Mumbai", "Chennai", "Hyderabad"])
# print(df3)

# for i in range(5):
#     if df3.iloc[i, 1] < 600 and df3.iloc[i, 2] >7000:
#         print(df3.iloc[i])
#     else: continue

# print(df3.iloc[0, 1])

dataDict3 = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    "X": ["Mathematics", "Science", "S. Studies", "English", "Hindi", "Sanskrit"],
    "XII": ["Accountancy", "Hindi/IP", "English", "B. Studies", "Economics", "NaN"]
}

df4 = pd.DataFrame(dataDict3, index=range(1,7))
# print(df4)

for i in range(6):
    if df4.iloc[i, 1] == "Sanskrit":
        df4.iloc[i,2] = "IP"

    else:continue

print(df4)
