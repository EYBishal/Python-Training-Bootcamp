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
