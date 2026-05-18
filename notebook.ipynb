# Import libraries
import pandas as pd
from matplotlib import pyplot as plt

# Load the CSV data into DataFrames
super_bowls = pd.read_csv("datasets/super_bowls.csv")
tv = pd.read_csv("datasets/tv.csv")
halftime_musicians = pd.read_csv("datasets/halftime_musicians.csv")

#merge tables
viewership = pd.merge(super_bowls, tv, on='super_bowl')

# convert date column to datetime
viewership['date'] = pd.to_datetime(viewership['date'])

# sort by date
viewership = viewership.sort_values('date')

# check if viewership generally increased over time
viewership_increased = bool(viewership['avg_us_viewers'].iloc[-1] > viewership['avg_us_viewers'].iloc[0])
print('viewership_increased: ', viewership_increased)

# point difference greater than 40
difference = int((super_bowls['difference_pts'] > 40).sum())
print('difference: ', difference)

# who performed the most songs
most_songs = halftime_musicians.sort_values('num_songs', ascending=False)['musician'].iloc[0]
print('most_songs: ', most_songs)
