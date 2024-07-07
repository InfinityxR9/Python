import matplotlib.pyplot as plt

date = ["25/12", "26/12", "27/12"]
temp = [8.5, 10.5, 6.8]

plt.plot(date, temp, '.')
plt.xlabel("Date")
plt.ylabel("temp in degree celsius")
plt.title("WTF")
plt.grid(True)
plt.yticks(temp)
plt.xticks(date)

plt.show()

