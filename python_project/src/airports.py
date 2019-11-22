# From this jupyter-notebook I'll take a list of latitudes and another of longitudes, to implement in main.ipynb
## it contains further information of mean of transportations that i'll also use

import pandas as pd
import os

print(os.getcwd())

data = pd.read_csv ("./input/airports-extended.csv")
print(data)
