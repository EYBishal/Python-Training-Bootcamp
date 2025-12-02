import pandas as pd

df=pd.read_csv("retail_sales.csv")

df["Date"]= pd.to_datetime(df["Date"]) #converted into date time format
print(df.info())
df["year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day"]=df["Date"].dt.day

high_ele=df[(df["Category"] =="Electronics") & (df["TotalPrice"] > 1000)]
print(high_ele)

so=df.sort_values("TotalPrice",ascending=False)

print(so)

cat=df.groupby("Category")["TotalPrice"].sum()
print(cat)

st=df.groupby("Store")["TotalPrice"].mean()
print(st)

ci=df.groupby("City")["OrderID"].count()
print(ci)
