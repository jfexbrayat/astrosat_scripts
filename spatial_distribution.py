"""
04/08/2018 - JFE
This script plots maps of fire distribution seen by MODIS and VIIRS during 2013-2017
"""

# import modules
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import AxesGrid

# import projection, features and utils from cartopy
from cartopy.crs import PlateCarree
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.feature import BORDERS, LAND, LAKES
from cartopy.mpl.geoaxes import GeoAxes

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

# define projection for the maps... use PlateCarre
axes_class = (GeoAxes,dict(map_projection=PlateCarree()))

# instantiate a figure and clear figure in case we're in an interactive session
fig = plt.figure('fire distribution');fig.clf()

# create an axesgrid for the maps
mapgrid = AxesGrid(fig,111,nrows_ncols=(1,2),axes_class=axes_class, \
label_mode='',axes_pad=0.5)

# store the name of the datasets in a list
df_names = ['a) MODIS','b) VIIRS']
BORDERS.scale = '10m'
LAND.scale = '10m'
LAKES.scale='10m'

# loop over dataframes to plot
for ii, df in enumerate([df_modis,df_viirs]):

    # assign axis to variable for simplicity
    ax = mapgrid[ii]

    # scatter plot with colour coding the doy
    ax.scatter(df.longitude,df.latitude,s=.05,c='grey')

    # make the map look nicer with high res coastlines, borders and land mask
    ax.coastlines(resolution = '10m')
    ax.add_feature(BORDERS)
    ax.add_feature(LAND)
    ax.add_feature(LAKES)

    # set ticks
    ax.set_xticks(range(-92,-88,1),crs=PlateCarree())
    ax.xaxis.set_major_formatter(LongitudeFormatter())

    ax.set_yticks(range(14,18,1),crs=PlateCarree())
    ax.yaxis.set_major_formatter(LatitudeFormatter())

    # set title
    ax.set_title(df_names[ii])

    ax.grid(True,ls=':')

#save figure
fig.savefig('../figures/spatial_distribution.png',bbox_inches='tight')
