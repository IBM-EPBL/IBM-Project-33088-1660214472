# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ra5f8vEiYH3X-Wi-3b9kdZqRw9_sGK3V
"""

import numpy as np

import pandas as pd

df = pd.read_csv("Churn_Modelling.csv")

df

df["NumOfProducts"].value_counts()

df.shape

df.columns

df["Geography"].value_counts()

df.dtypes

df.info()

df.head()

df.describe()

df.tail()

df.isnull().sum()

df.corr()

import matplotlib.pyplot as plt

import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

plt.figure(figsize=(7,7))
sns.countplot(x= "Tenure" , data=df)
plt.xlabel("0: Customer with bank, 1: exited from bank")
plt.ylabel(" Count of customers")
plt.title("Bank Customers Viz")
plt.show()

plt.scatter(df.CreditScore, df.Tenure)

df.columns

plt.scatter(df.Balance,df.CreditScore)

plt.scatter(df.Age, df.EstimatedSalary)

df.columns

df.head()

df.columns

df.head()

df.info()