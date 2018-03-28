# modules we'll use
import pandas as pd
import numpy as np
import seaborn as sns
import datetime
import matplotlib.pyplot as plt

# read in our data
earthquakes = pd.read_csv("data/database.csv")
landslides = pd.read_csv("data/catalog.csv")
volcanos = pd.read_csv("data/database.csv")

# set seed for reproducibility
np.random.seed(0)

# print the first few rows of the date column
print(landslides['date'].head())

# check the data type of our date column
print(landslides['date'].dtype)

# create a new column, date_parsed, with the parsed dates
landslides['date_parsed'] = pd.to_datetime(landslides['date'], format = "%m/%d/%y")

# print the first few rows
print(landslides['date_parsed'].head())



# try to get the day of the month from the date column
#  We're getting this error because the dt.day() function doesn't know how to deal with a column with the dtype "object"
# day_of_month_landslides = landslides['date'].dt.day
# print(day_of_month_landslides)


# get the day of the month from the date_parsed column
day_of_month_landslides = landslides['date_parsed'].dt.day
print(day_of_month_landslides.head())

# remove na's
day_of_month_landslides = day_of_month_landslides.dropna()
# plot the day of the month
sns.distplot(day_of_month_landslides, kde=False, bins=31)
plt.show()