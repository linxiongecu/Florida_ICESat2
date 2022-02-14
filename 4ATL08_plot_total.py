"""

This example code illustrates how to access and visualize an NSIDC 
ICESat-2 ATL08 L3A version 4 HDF5 file in Python.

If you have any questions, suggestions, or comments on this example, please use
the HDF-EOS Forum (http://hdfeos.org/forums).  If you would like to see an
example of any other NASA HDF/HDF-EOS data product that is not listed in the
HDF-EOS Comprehensive Examples page (http://hdfeos.org/zoo), feel free to
contact us at eoshelp@hdfgroup.org or post it at the HDF-EOS Forum
(http://hdfeos.org/forums).

Usage:  save this script and run

   $python ATL08_20210114234518_03361001_004_01.h5.py

The HDF5 file must in your current working directory.

Tested under: Python 3.7.7 :: Anaconda custom (64-bit)
Last updated: 2021-05-04
"""

import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import csv
import h5py
def ATL08plot(lon, lat, h, fi):
    #FILE_NAME = 'FloridaData/data/processed_ATL08_20181017085235_02860107_005_01.h5'
        #f=FILE_NAME
        
    
       
##        datavar = h
##        data = datavar[:]
##        units = datavar.attrs['units']
##        long_name = datavar.attrs['long_name']
##        _FillValue = datavar.attrs['_FillValue']
       
##        # Handle FillValue
##        data[data == _FillValue] = np.nan
##        data = np.ma.masked_where(np.isnan(data), data)
        data = h
        # Find the middle location.
        lat_m = lat[int(lat.shape[0]/2)]
        lon_m = lon[int(lon.shape[0]/2)]

        # Let's use ortho projection.
        orth = ccrs.Orthographic(central_longitude=lon_m,
                                 central_latitude=lat_m,
                                 globe=None)
        orth = ccrs.Miller(central_longitude=lon_m,
                                 globe=None)
        
        ax = plt.axes(projection=orth)
        
        # Remove the following line to see a zoom-in view.
        ax.set_global()
        #25.055195484759203, -84.40967872677047
        #29.459354197571287, -78.35650775817035
        #ax.set_extent([canada_west, canada_east, canada_south, canada_north])
        ax.set_extent([-83, -79,24, 27])

        # Plot on map.
        p = plt.scatter(lon, lat, c=data, s=1, cmap=plt.cm.jet,
                        transform=ccrs.PlateCarree())

        # Put grids.
        gl = ax.gridlines(draw_labels=True, dms=True)

        # Put coast lines.
        ax.coastlines()

        # Put grid labels at left and bottom only.
        gl.top_labels = False
        gl.right_labels = False

        # Put degree N/E label.
        gl.xformatter = LONGITUDE_FORMATTER
        gl.yformatter = LATITUDE_FORMATTER

        # Adjust colorbar size and location using fraction and pad.
        cb = plt.colorbar(p, fraction=0.022, pad=0.01)
        #units = units.decode('ascii', 'replace')        
        cb.set_label(data, fontsize=8)
        
        basename = fi
        #long_name = long_name.decode('ascii', 'replace')        
        plt.title('{0}'.format(basename))
        
        fig = plt.gcf()
        plt.show(block=False)
        plt.pause(3)
        plt.close()
        #pngfile = "{0}.py.png".format(basename)
        #fig.savefig(pngfile)




