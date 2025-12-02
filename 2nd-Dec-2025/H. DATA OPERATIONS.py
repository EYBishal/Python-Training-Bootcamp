import pandas as pd
import numpy as np
from pandas import pivot_table
import matplotlib.pyplot as plt
df=pd.read_csv("superstore.csv")


#Extract year, month, day from OrderDate.

'''
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.month
df['Day'] = df['OrderDate'].dt.day
print(df.head())'''



#Calculate which day of week each order was placed.
'''
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Day'] = df['OrderDate'].dt.day_name()
print(df[['OrderID', 'OrderDate', 'Day']].head())'''



#Find orders shipped in more than 5 days.

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['ShipDate'] = pd.to.df['ShipDate'] = pd.to_datetime(df['ShipDate'])
df['ShipDuration'] = (df['ShipDate'] - df['OrderDate']).dt.days
dd = df[df['ShipDuration'] > 5]



#Group orders by month and compute sales.

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['YearMonth'] = df['OrderDate'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('YearMonth')['Sales'].sum().reset_index()
print(monthly_sales)



#Plot sales trend per month (line chart).



plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['YearMonth'], monthly_sales['Sales'], marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
