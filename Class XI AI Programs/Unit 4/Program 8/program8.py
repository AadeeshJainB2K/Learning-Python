import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv("./rainfall.csv")

x = df["Month"]
y = df["Rainfall_mm"]

plt.xlabel("Month")
plt.ylabel("Rainfall_mm")
plt.bar(x, y, color="skyblue")
plt.show()
