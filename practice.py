import pandas as pd
import numpy as np

#  Reading data
bpd=pd.read_csv('bpdata/Building_Permits.csv')
nfld=pd.read_csv('nfldata/NFL Play by Play 2009-2017 (v4).csv')


# set seed for reproducibility
np.random.seed(0)

# look at a few rows of the nfl_data file. I can see a handful of missing data already!
# print(nfld.sample(5))

#  See how many data points we have

# get the number of missing data points per column nfl data
missing_values_count = nfld.isnull().sum()
# print(missing_values_count)

# look at the # of missing points in the first ten columns
# print(missing_values_count[0:10])

# how many total missing values do we have?
total_cells = np.product(nfld.shape)
totalMissingValue=missing_values_count.sum()
# print(totalMissingValue)

# percent of data that is missing
# print((totalMissingValue/total_cells) * 100)


# dropping all rows with with one missing value
# nfld.dropna()  all rows drop bcz evry row had one missing value

# remove all columns with at least one missing value
columns_with_na_dropped = nfld.dropna(axis=1)
# print(columns_with_na_dropped.head())

# just how much data did we lose?
# print("Columns in original dataset: %d \n" % nfld.shape[1])
# print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])

#                     FIlling In Missing values automatically
# get a small subset of the NFL dataset
subset_nfl_data = nfld.loc[:, 'EPA':'Season'].head()
# print(subset_nfl_data)

# replace all NA's with 0
# print(subset_nfl_data.fillna(0))

# replace all NA's the value that comes directly after it in the same column,
# then replace all the reamining na's with 0
# subset_nfl_data.fillna(method = 'bfill', axis=0).fillna("0")