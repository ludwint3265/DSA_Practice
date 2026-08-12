import sqlite3  as sq
import numpy as np
import sklearn as sk
import matplotlib as plt
import scipy as sp

# Remember to study basic database operations in SQL and data manipulation in Pandas
#
# Pandas is an open-source Python data analysis and
# manipulation module. It has features such as DataFrames / Series
# (pandas objects that allow for data manipulation with integrated 
# indexing)
#
# SQLite is a C library that provides a lightweight disk-based database
# that doesn't require a separate process, and allows accessing the 
# database using a SQL-like language. sqlite3 is a Python module that
# provides a SQL interface compliant with the DB-API 2.0 specification
# described by PEP 249.
#
# NumPy is a Python library that provides multidimensional arrays, derived 
# array objects such as matrices and masked arrays, and functions for 
# fast operations on arrays like mathematics, sorting, selecting, linear 
# algebra, and more
# 
# Scikit-learn is a Python library that supports supervised and 
# unsupervised learning for building models. It also provides tools
# for model fitting, data preprocessing, model selection and evaluation,
# and more.
#
# Matplotlib is a Python library used for making static, animated, 
# and interactive visualizations in Python. 
# 
# Scipy is a Python library that has mathematical algorithms and 
# and functions built on NumPy. It provides the user with high-level 
# commands and classes for manipulating and visualizing data.

# Pandas
import pandas as pd
df = pd.DataFrame(
   {
      "Name": [
         "S, Joseph",
         "P, Marlon",
         "J, Bryan",
         "P, Lisbeth",
         "M, Chris",
         "T, Ludwin",
      ],
      "Age": [0, 19, 20, 21, 20, 21],
      "Height": [6.2, 5.8, 5.6, 5.3, 5.10, 5.3],
      "Sex": ["male", "male", "male", "female", "male", "male"]
   }
)

print(df)
# Each column in a DataFrame is a Series

# Print 
print(df["Age"])

my_ages = pd.Series([20,70,40,30], name = "Ages")
print(my_ages)
my_heights = pd.Series([12,2,4,23,40], name = "Heights")
# Series have no column labels, but it does have row lab

# get max age of DataFrame and Series
print(df["Age"].max())
print(my_ages.max())

print(df.describe())
print(df.head(1))
print(df[df.Name == "S, Joseph"])
print(df.iloc[2:4])

print(pd.melt(df))
print(df.pivot(columns='Name',values="Height"))
