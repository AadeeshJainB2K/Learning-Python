import matplotlib.pyplot as plt
Test = [1, 2, 3, 4, 5]
Marks = [25, 34, 49, 40, 48]

plt.title("Marks Obtained")

plt.xlabel("Test")
plt.xticks(Test)
plt.yticks(Marks)
plt.ylabel("Marks")
plt.plot(Test,Marks,'k',marker=".")
plt.show()