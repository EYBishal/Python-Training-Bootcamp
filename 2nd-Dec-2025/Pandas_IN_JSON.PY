import pandas as pd

df=pd.DataFrame({
    "Name":["Bishal","Arun"],
    "Marks":[98,99],
    "City":["Mumbai","Kolkata"]

})

df.to_json("students.json",orient="records",indent=4)
print("Json file created")

df=pd.read_json("students.json")
print("succesfully read json file")
print(df)
#################################################

import pandas as pd

df=pd.read_csv("retail_sales.csv")

#print(df.head())
#Describe = It gives summary statistics for numeric columns:like count,mean,avg etc


#print(df.describe())
#print(df.info())
#info  Shows:Number of entries (rows)Column Memory usage
#print(df.isnull().sum())
#check for null value-- isnull() and sums them --sum()

df["Date"]= pd.to_datetime(df["Date"]) #converted into date time format
print(df.info())
df["year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day"]=df["Date"].dt.day
