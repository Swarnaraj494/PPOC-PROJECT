import matplotlib.pyplot as plt
x = ["A","B","C"]
h = [2,3,4] 
c = ["red","blue","green"]
plt.bar(x,h,width=0.4,color=c)
plt.xlabel("Alphabets")
plt.ylabel("Numbers")
plt.title("Example of bar graph")
plt.show()