import matplotlib.pyplot as plt

# Creating the dataset
categories = ['Category A', 'Category B', 'Category C']
feature1 = [10, 15, 20]
feature2 = [5, 8, 12]
feature3 = [3, 6, 9]

fig = plt.figure(figsize=(10, 5))

plt.bar(categories, feature1, color='r', width=0.25)
plt.bar(categories, feature2, color='g', width=0.25)
plt.bar(categories, feature3, color='b', width=0.25)

plt.xlabel("Categories")
plt.ylabel("Features")
plt.title("Small Dataset with 3 Features")


plt.legend(["Feature 1", "Feature 2", "Feature 3"])

plt.show()
