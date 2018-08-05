# astrosat_scripts
Scripts to visualize active fire data from FIRMS over Guatemala

Scripts below have to be placed in a folder so that they can access the
dataset in the ../data/ directory and save figures in a ../figures/ directory

Easiest is to clone in the astrosat_data_science_test folder using
"git clone https://github.com/jfexbrayat/astrosat_scripts.git"

# Overview of scripts

fire_seasonality.py
produces a barplot of fraction of fire in each calendar monthly

frp_timeseries.py
produces time series of monthly median specific fire radiative power

spatial_distribution.py
plots maps of detected fires

summary.py
prints a summary of datasets with number of fires and distribution according to
the three confidence classes

# Required python modules

The scripts work with the following modules under Python 3.6.1

Cartopy==0.16.0 #high resolution shapefiles and masks may have to be downloaded
when running the code for the first time, which will raise a warning

matplotlib==2.0.2

pandas==0.20.1

scipy==0.19.0
