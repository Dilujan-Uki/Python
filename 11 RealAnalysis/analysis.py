import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

#Loading a CSV file into a DataFrame
df = pd.read_csv("./11 RealAnalysis/tips.csv");


#Displaying the first 5 rows of the DataFrame
print(df.head());

# Show first few rows
print(df.head())

# NumPy calculation on Pandas data
average_tip = np.mean(df["tip"])
print("Average tip:", average_tip)

# Create a plot
plt.scatter(df["total_bill"], df["tip"])
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Tip vs Total Bill")
plt.show();