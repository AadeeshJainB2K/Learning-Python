import matplotlib.pyplot as plt

a = ["Oxford", "Delhi", "Jyothis", "Sanskriti", "Bombay"]
b = [123, 87, 105, 146, 34]

plt.xlabel("University")
plt.ylabel("Number")

plt.bar(a, b, color="skyblue")
plt.show()