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
