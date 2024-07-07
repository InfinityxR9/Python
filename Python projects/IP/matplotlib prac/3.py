import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./data.csv")

# only this line to be written using pandas
data.plot(kind="line", color=['red', 'blue', 'green'], marker="*", markersize=15, linestyle="--", linewidth=0.5)

plt.grid(True)
plt.xlabel("Days")
plt.ylabel("Sales")
# print(data.Week_1, data.Week_2, data.Week_3)


# To get the different values of sales for Y-ticks
arrTicks = []
def addLis(*arr):
    for n in arr:
        for i in n:
            if i not in arrTicks:
                arrTicks.append(i)

addLis(data.Week_1, data.Week_2, data.Week_3)

# arrTicks.sort()
print(arrTicks)

ticks = data.index.tolist()
plt.xticks(ticks, data.Day)
plt.yticks(arrTicks)

plt.title("Sales data")
plt.show()
