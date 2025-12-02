import pandas as pd
import numpy as np
df=pd.read_csv("superstore.csv")

#21. Total Sales per Region.
'''
total_sales_region = df.groupby("Region")["Sales"].sum()
print(total_sales_region)
'''

#22. Average Profit per Category.
'''
av=df.groupby("Category")["Profit"].mean()
print(av)
'''
#23. Count of orders per Customer.

'''
co=df.groupby("Customer")["Order"].count()
print(co)
'''

#24. Sum of Sales per Segment.

'''
so=df.groupby("Segment")["Sales"].sum()
print(so)
'''


#25. Total Quantity sold per SubCategory.
'''
quantity_subcategory = df.groupby("SubCategory")["Quantity"].sum()
print(quantity_subcategory)'''

#26. Mean ShippingDays grouped by Category.
'''

df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df["ShipDate"] = pd.to_datetime(df["ShipDate"], errors="coerce")
df["ShippingDays"] = (df["ShipDate"] - df["OrderDate"]).dt.days

mean_shipping_category = df.groupby("Category")["ShippingDays"].mean()
print(mean

'''
