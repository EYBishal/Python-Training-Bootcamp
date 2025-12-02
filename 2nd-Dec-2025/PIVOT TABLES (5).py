import pandas as pd
import numpy as np
from pandas import pivot_table

df=pd.read_csv("superstore.csv")

#Create pivot: Rows = Region, Columns = Category, Values = Sales.

'''
pivottable=pd.pivot_table(df,index='Region',
                          columns='Category',
                          values='Sales',
                          aggfunc='sum')

print(pivottable)
'''

#Pivot showing Profit by SubCategory and Segment.
'''
pi=pivot_table(df,
               index='SubCategory',
               columns='Segment',
               values='Profit',
               aggfunc='sum')
print(pi)
'''


#Pivot showing count of orders by Returned status and Region.
'''
pi=pivot_table(df,
               index='Returned',
               columns='Region',
               values='OrderID',
               aggfunc='count')
print(pi)'''


#Pivot showing average UnitPrice per Category.

'''
pi=pivot_table(df,
               index='Category',
               values='UnitPrice',
               aggfunc='mean')

print(pi)'''

#Pivot showing total Quantity per Month and Region.

'''
pi=pivot_table(df,
               index='Region',
               columns='Month',
               values='Quantity',
               aggfunc='sum')
print(pi)'''
