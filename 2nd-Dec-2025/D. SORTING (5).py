import pandas as pd
import numpy as np
df=pd.read_csv("superstore.csv")

#16. Sort by Sales descending.
'''
df=df.sort_values(by=['Sales'], ascending=False)
print(df)
'''

#17. Sort by ProfitMargin.
'''
df=df.sort_values(by=['Profit'], ascending=False)
print(df)'''

#18. Sort by Region then City.

'''
df = df.sort_values(by=["Region", "City"], ascending=[True, True])
print(df)
'''

#19. Sort by ShippingDays largest to smallest.
'''
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
df=df.sort_values(by=['ShipDate'], ascending=False)
print(df)
'''

#20. Sort by CustomerName alphabetical.
'''
df=df.sort_values(by=["CustomerName"], ascending=False)
print(df["CustomerName"])
'''
