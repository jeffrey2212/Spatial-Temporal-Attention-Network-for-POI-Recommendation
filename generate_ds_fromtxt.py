import pandas as pd
import numpy as np
from datetime import datetime

# Replace 'path_to_your_data.txt' with the path to your dataset file
data_path = 'data/loc-gowalla_totalCheckins.txt'

# Read the dataset
df = pd.read_csv(data_path, sep='\t', header=None, names=['user', 'check-in_time', 'latitude', 'longitude', 'location_id'])

# Convert 'check-in_time' to datetime
df['check-in_time'] = pd.to_datetime(df['check-in_time'])

# Assuming you want to calculate minutes since the first check-in in the dataset
min_time = df['check-in_time'].min()

# Calculate 'time in minutes' relative to the first timestamp
df['time_in_minutes'] = (df['check-in_time'] - min_time).dt.total_seconds() / 60

# Select and rename the columns to match the required format [user id, check-in location id, time in minutes]
final_df = df[['user', 'location_id', 'time_in_minutes']]

# Convert the DataFrame to a NumPy array
final_array = final_df.to_numpy()

# Save the array as a .npy file
np.save('data/gowalla.npy', final_array)

print('Data processing complete. File saved as processed_data.npy')
