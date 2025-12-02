import pandas as pd
import numpy as np
df=pd.read_csv("superstore.csv")

#1. Load the CSV and display first 10 rows.
print(df.head(10))


#2. Show total number of rows and columns.
print(df.shape)

#3. Find data types of each column.
print(df.describe()) #or we can use print(df.info())

#4.Identify columns containing missing values.
print(df.isnull().sum())


#5. Convert OrderDate and ShipDate to datetime.
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
print(df.info())
