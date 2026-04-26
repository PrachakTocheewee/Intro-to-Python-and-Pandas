#read crv file
# Introduction to Pandas
# imorting the library
import pandas as pd
import numpy as np
# Update line 6 to this:
penguins = pd.read_csv("sample_data/penguins.csv")

# And don't forget to wrap line 7 in a print() to see it!
#head() and tail() functions select the first and last 5 rows of the data frame, respectively.
print(penguins.head())
print(penguins.tail())
#shape of data frame
print(penguins.shape)
#info of data frame
print(penguins.info())
print(penguins.info())