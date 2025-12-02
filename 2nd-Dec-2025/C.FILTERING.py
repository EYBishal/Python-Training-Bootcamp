import pandas as pd
import numpy as np
df=pd.read_csv("superstore.csv")

#11. Filter all orders from the West region.
'''
df=df[df["Region"]=="West"]
print(df.head())
'''

#12. Filter Technology category with Sales > 400.
'''
df=df[(df["Category"] =="Technology") & (df["Sales"] > 400)]
print(df.head())
'''

#13. Find all products returned by customers.
'''
pro=df[df["Returned"]=="Yes"]["ProductName"]
print(pro)
'''



#14. Show Furniture orders shipped after 2024-01-20.

'''
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
fo=df[(df["Category"]=="Furniture") & (df["ShipDate"] > pd.to_datetime("2024-01-20"))]
print(fo)
'''

#15. Filter orders where Profit < 20.


df = df[df["Profit"] < 20]
