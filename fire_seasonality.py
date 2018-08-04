"""
04/08/2018 - JFE
This script plots bars representing the seasonality fire distribution seen
by MODIS and VIIRS during 2013-2017
"""

# import modules
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr

# read the csv with data
df_modis = pd.read_csv('../data/fire_archive_M6_12555.csv')
df_viirs = pd.read_csv('../data/fire_archive_V1_12556.csv')

# set the index to a datetime index series
df_modis.index = pd.to_datetime(df_modis["acq_date"])
df_viirs.index = pd.to_datetime(df_viirs["acq_date"])
df_viirs = df_viirs['2013-01-01':'2017-12-31']  #remove data for 1/1/2018

# filter out the low confidence
df_modis = df_modis.loc[df_modis.confidence >= 30]
df_viirs = df_viirs.loc[df_viirs.confidence != 'l']

# create a new dataframe which holds fire counts
df_summary = pd.DataFrame(index=range(1,13))

# save counts as fractions
df_summary['MODIS'] = df_modis.latitude.groupby(df_modis.index.month).count() / df_modis.shape[0]
df_summary['VIIRS'] = df_viirs.latitude.groupby(df_viirs.index.month).count() / df_viirs.shape[0]

#print dataset
print(df_summary)

# print correlation between datasets
print(df_summary.corr())

# plot using the df method
df_summary.plot(kind='bar',color=['blue','red'],figsize=(8,4),width=.8)

plt.ylabel('fraction of total active fires detected')
plt.xlabel('month')

#use month initials
plt.xticks(range(12),['J','F','M','A','M','J','J','A','S','O','N','D'],rotation=0)

plt.savefig('../figures/fire_seasonality.png',bbox_inches='tight')
