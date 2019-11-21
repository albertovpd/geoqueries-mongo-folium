# the dataset is called "airports", but it is completed with other facilities
# https://www.kaggle.com/open-flights/airports-train-stations-and-ferry-terminals#airports-extended.csv
import pandas as pd
data = pd.read_csv ("input/airports-extended.csv")

null_cols = data.isnull().sum()
drop_cols = list(null_cols[null_cols > 35000].index)
data_clean1 = data.drop(drop_cols, axis=1)
data.dropna()

# Trasposing the matrix to rename the columns without loosing elements
data=data.reset_index().T.reset_index().T
data_coord=data.rename(columns={7:"latitude",8:"longitude"})

'''# Creating a list of names as long as the list of coordinates
facilities=[]
for e in data_coord["latitude"]:
    facilities.append("airport")

#I have some str-types that I must turn into float
def type_conversor(x):
    for e in data_coord[x]:
        e=float(e)

type_conversor("latitude")
type_conversor("longitude")'''