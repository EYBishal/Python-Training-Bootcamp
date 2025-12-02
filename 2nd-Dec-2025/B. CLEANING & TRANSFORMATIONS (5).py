import pandas as pd
import numpy as np
df=pd.read_csv("superstore.csv")

#6. Create a new column ShippingDays = ShipDate - OrderDate.
'''
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShippingDays"]=(df["ShipDate"]-df["OrderDate"]).dt.days
print(df.head())
'''


# 7.Create ProfitMargin = Profit / Sales.

'''
df["ProfitMargin"]=df["Profit"]/df["Sales"]
print(df.head())
'''

#8. Standardize CustomerName to title case.
'''
df["CustomerName"]=df["CustomerName"].apply(lambda x:str(x).title())
# we can use this also  df["CustomerName"] = df["CustomerName"].str.title
print(df["CustomerName"])
'''

#9.Remove rows where Sales is zero or negative.
'''
df["Sales"]=df["Sales"].apply(lambda x:"Unknown" if x<0 else x)
df=df[df["Sales"]>0]
print(df.head())
'''

#10. Convert Discount from decimal to percentage format.

df["Discount"]=df["Discount"].apply(lambda x:x*100)
print(df.head())
