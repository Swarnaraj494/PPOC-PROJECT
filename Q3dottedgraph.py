import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 6, 2, 8, 5]


plt.scatter(x, y, color='red')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot of Points")


plt.plot(x, y, color='blue')

plt.show()
