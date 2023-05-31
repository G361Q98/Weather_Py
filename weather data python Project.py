# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:01:49 2023

@author: hp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('Weather Data.CSV')
data.head()
data.shape
data.index
data.columns
data.dtypes
data['Weather'].unique()
data.nunique()
data.count()
data['Weather'].value_counts()
data.info()
# find all the unique "Wind speed" values in data
data.head(2)
data.nunique()
data['Wind Speed_km/h'].nunique()
data['Wind Speed_km/h'].unique() #Answer
# find the number of times when weather is exactly clear
data.head(2)
#value Count()
data.Weather.value_counts()
#filtering
data[data.Weather=='Clear']
#groupby
data.groupby('Weather').get_group('Clear')
#find the number of times when wind speed was exactly 4 km/hr 
data.head(2)
data[data['Wind Speed_km/h']==4]#Answer
#find out the null values in the data
data.isnull().sum()
#Rename the column name 'weather' of dataframe column to 'weather condition'
data.head(2)
data.rename(columns = {'Weather':'Weather Condition'}, inplace = True)
#What is mean 'visibility'?
data.head(2)
data.Visibility_km.mean()
#What is the standard Deviation of 'Pressure' in this data?
data.Press_kPa.std()
#What is the Variance of 'Relative Humidity' in this data

data['Rel Hum_%'].var()
# Find all the instances when snow was recorded
#value count
data.head(2)
data['Weather Condition'].value_counts()
data[data['Weather Condition'] == 'Snow']
data[data['Weather Condition'].str.contains('Snow')]
#find all instances when 'wind speed is above 24' and 'visibility is 25'
data.head(2)
data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]
#What is mean value of each column against each 'weather condition'
data.head(2)
data.groupby('Weather Condition').mean()
#What is the minimum and maximum value of each column against each 'Weather condition'
data.head(2)
data.groupby('Weather Condition').min()
data.groupby('Weather Condition').max()
#Show all the records when weather condition is fog
data[data['Weather Condition'] == 'Fog']
# find all the instances when 'weather is clear' or'Visibility is above 40'
data[(data['Weather Condition'] == 'Clear') |(data['Visibility_km'] > 40)]
#find all the instances when weather is clear and Rel humidity is greater than 50
#or visibility is above 40
data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)]