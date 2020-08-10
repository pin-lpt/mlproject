import pandas as pd
from tensorflow.keras import to_categorical

def to_date_time_data(data):
	data = pd.to_date_time(data)
	return data

def to_cat(y):
	y = to_categorical(y)
	return y
