import pandas as pd
import numpy as np
from pandas import pivot_table

df=pd.read_csv("superstore.csv")





#Create a discount lookup: Consumer=5, Corporate=8, Home Office=10 and merge it.
'''
discount_df = pd.DataFrame({
    'Segment': ['Consumer', 'Corporate', 'Home Office'],
    'Discount': [5, 8, 10]
})


df=pd.merge(df,discount_df,on='Segment',how='left')
print(df)'''

#Create a region tax table and merge.
'''
discount_df = pd.DataFrame({
    'Region': ['East', 'West', 'North','South'],
    'Discount': [5, 8, 10,12]
})


df=pd.merge(df,discount_df,on='Region',how='left')
print(df)'''

#Merge customer-level totals into the main df.

'''
customer_totals = df.groupby('CustomerName')[['Sales','Quantity','Profit']].sum()
df=pd.merge(df,customer_totals,on='CustomerName',how='left')
print(df)'''

#Merge product-level profitability summary.
'''
product_profit=df.groupby('ProductName')[['Sales','Profit']].sum()
df=pd.merge(df,product_profit,on='ProductName',how='left')
print(df)'''
