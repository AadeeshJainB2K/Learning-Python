import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv("rainfall.csv")
x = df["Month"]
y = df["Rainfall_mm"]

wp = {"linewidth":"1","edgecolor":"k"}

plt.pie(y,labels= x ,wedgeprops=wp)
plt.show()