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
#check for missing values
print(penguins.isnull().sum())
#drop missing values
penguins = penguins.dropna()
print(penguins.shape)
print(penguins.info())
#describe data frame
print(penguins.describe())
penguins["avg_bill_mm"] = (penguins["bill_length_mm"] + penguins["bill_depth_mm"]) / 2
penguins.head()
penguins.tail()

#write csv file
penguins.to_csv("sample_data/penguins_with_avg_bill.csv", index=False)