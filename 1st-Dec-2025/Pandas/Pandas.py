#pandas used to create, transformations, manipulate,delete data
#pandas focus on two ds 1--series, 2---dataframe

import pandas as pd

#series
s=pd.Series([1,2,3,4,5,6])
print(s)

#dataframe
#must have same amount of value for every key to create a 2d figure
data={
    "Name":["Bishal","Rahul"],
    "Marks":[1,2]
}

df=pd.DataFrame(data)
print(df)

####################################################

import pandas as pd

data={
    "Name":["Bishal","Arun","Subham"],
    "Marks":[87,98,96],
    "city":["Kolkata","Mumbai","Delhi"]}



df=pd.DataFrame(data)

df.to_csv("students.csv",index=False)
print("file Created")


####################################################

import pandas as pd

df=pd.read_csv("students.csv")

print(df)

##############################################

import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

print(df)

print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.describe())

###################################################

import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

print(df)


df["result"] =df["Marks"].apply(lambda x: "Pass" if x > 70 else "Fail")
print(df)

sorted_df=df.sort_values(by="Marks", ascending=False)
print(sorted_df)

########################################################

import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

print(df)

df2=df.copy()
df2.loc[2,"City"]= None
print(df2)
print(df2.isnull().sum())

df2_filled =df2.fillna("Unknown")
print(df2_filled)
