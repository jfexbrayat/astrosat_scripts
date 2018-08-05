"""
05/08/2018 - JFE
This script print some statistics for the MODIS and VIIRS active fires data
for Guatemala
"""

import pandas as pd

#load data and assign index to dates
df_modis = pd.read_csv('../data/fire_archive_M6_12555.csv')
df_modis.index = pd.to_datetime(df_modis['acq_date'])

df_viirs = pd.read_csv('../data/fire_archive_V1_12556.csv')
df_viirs.index = pd.to_datetime(df_viirs['acq_date'])
df_viirs = df_viirs['2013-01-01':'2017-12-31'] #remove few records for 2018-01-01

# print the number of fires in each classes for MODIS
print('# MODIS detections:', df_modis.shape[0])
print('# MODIS low confidence: ', (df_modis.confidence < 30.).sum())
print('# MODIS nominal confidence: ', ((df_modis.confidence >= 30.) & (df_modis.confidence < 80)).sum())
print('# MODIS high confidence: ', (df_modis.confidence>=80).sum())

# same for VIIRS
print('\n# VIIRS detections:',df_viirs.shape[0])
print('# VIIRS low confidence: ', (df_viirs.confidence =='l').sum())
print('# VIIRS nominal confidence: ', (df_viirs.confidence == 'n').sum())
print('# VIIRS high confidence: ', (df_viirs.confidence == 'h').sum())
