"""
04/08/2018 - JFE
This script plots a monthly time series of fire radiative power
seen by MODIS and VIIRS during 2013-2017
"""

# import modules
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr

# read data files
df_modis = pd.read_csv('../data/fire_archive_M6_12555.csv')
df_viirs = pd.read_csv('../data/fire_archive_V1_12556.csv')

# remove low confidence retrievals
df_modis = df_modis.loc[df_modis.confidence >= 30.]
df_viirs = df_viirs.loc[df_viirs.confidence != 'l']

# convert frp from MW in pixel to W m-2 to be comparable
df_modis['frp_m2'] = df_modis.frp #MW km-2 is W m-2
df_viirs['frp_m2'] = 1e6*df_viirs.frp/(375.**2)

# set the index to a datetime object
df_modis.index = pd.to_datetime(df_modis.acq_date)
df_viirs.index = pd.to_datetime(df_viirs.acq_date)

# remove Jan 1st 2018 from viirs df
df_viirs = df_viirs['2013-01-01':'2017-12-31']

# resample to monthly values
modis_median = df_modis.frp_m2.resample('M').median()
viirs_median = df_viirs.frp_m2.resample('M').median()

# calculate correlation and std
print("Pearson's correlation: ", pearsonr(modis_median,viirs_median))
print('std MODIS: ', modis_median.std())
print('std VIIRS: ', viirs_median.std())

# instantiate a figure to plot median frp
plt.figure('time series');plt.clf()

#plot
modis_median.plot(color='blue',label='MODIS',style='-o',figsize=(8,4))
viirs_median.plot(color='red',label='VIIRS',style='-o',figsize=(8,4))

# adjust labels
plt.ylabel('Fire radiative power [W m$^{-2}$]')
plt.xlabel('Date')

# adjust figure and set legend
plt.ylim(0,50)
plt.legend(loc='lower left')

plt.grid(True,ls=':')

plt.savefig('../figures/frp_timeseries.png',bbox_inches='tight')
