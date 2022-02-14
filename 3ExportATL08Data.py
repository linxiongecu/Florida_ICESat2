#!/usr/bin/env python
# coding: utf-8

#import icepyx as ipx

import numpy as np

import xarray as xr

import pandas as pd

import h5py

import os,json

from pprint import pprint

import dask.dataframe as dd
import csv

# put the full filepath to a data file here. You can get this in JupyterHub by navigating to the file,

# right clicking, and selecting copy path. Then you can paste the path in the quotes below.
#import ATL08_plot


def read_atl08(fname, bbox=None):


###  Extract TIme Beam lat lon h_canopy h_te_mean 
        with h5py.File(fname, mode='r') as fi:
                #print("processing file: " + str(fi))
                # table initial
                df = pd.DataFrame()
                #print("Keys: %s" % fi.keys())       
                time = fi['/ancillary_data/data_start_utc'][0][0:10].decode('UTF-8')
                # Each beam is a group
                group = ['/gt1l', '/gt1r', '/gt2l', '/gt2r', '/gt3l', '/gt3r']
                # Loop trough beams
                for k,g in enumerate(group):
                    # 1) Read in data for a single beam #

                    #-----------------------------------#

                    # Load variables into memory (more can be added!)
                    # if beam not exist 
                   
                    if g[1:] not in list(fi.keys())  : continue
                            
                                  
                    # if land segment not exist 
                    if 'land_segments' not in list(fi[g].keys()):  continue
                                  
                    lat = fi[g+'/land_segments/latitude'][:]

                    lon = fi[g+'/land_segments/longitude'][:]

                    canopy_h = fi[g+'/land_segments/canopy/h_canopy'][:]
                    h_te_mean =  fi[g+'/land_segments/terrain/h_te_mean'][:]


                    #ATL08_plot.ATL08plot(lon, lat, h_te_mean, fi) 
                    #---------------------------------------------#

                    # 2) Filter data according region and quality #

                    #---------------------------------------------#

                    # Select a region of interest

                    if bbox:

                        lonmin, lonmax, latmin, latmax = bbox

                        bbox_mask = (lon >= lonmin) & (lon <= lonmax) & (lat >= latmin) & (lat <= latmax)

                    else:

                        bbox_mask = np.ones_like(lat, dtype=bool) # get all

                    # Test for no data

                    if len(canopy_h) == 0: continue

                    #-----------------------#

                    # 3) Save selected data #

                    #-----------------------#


                    # save as csv How much is the flow of people in Dalian http://mobile.120wtrlyy.com/

                    result = pd.DataFrame()
                    #print(time)
                    #result['time'] = time  
                    result['lon'] = lon
                    result['lat'] = lat
                    result['canopy_h'] = canopy_h
                    result['h_te_mean'] = h_te_mean
                    result.insert(0, 'beam', g[1:])
                   # result['beam'] = g[1:]
                   # extract time
                    result.insert(1, 'time', time)
                    #print(result)
                    frames = [df, result]
                    ##update df
                    df = pd.concat(frames)
                    #rows.append(result)
                    #print(df)
                    #print(pd.concat([rows, result]))
                   # rows = pd.concat(rows)
                    #print(pd.concat([rows, result]))
                    
                #print(fname[-49:-3])
                df.to_csv('CSV/' + fname[-49:-3] +'.csv', index=False)
        return df

#fname = 'Test/processed_ATL08_20181017085235_02860107_005_01.h5'
path = "C://Users//xiongl21//WorkingFolder//Postdoc//Icesat2//MyTutorial//FloridaData"
NameList = list(set(os.listdir(path)) - {'desktop.ini', 'whatever.ini'})
total = pd.DataFrame()


for fname in NameList:
    #print(fname)
    result = read_atl08(path+'//'+fname, None)
    # plot data
    
    #ATL08_plot.ATL08plot(path+'//'+fname)
    #print(result)
    frames = [total, result]
    ##update df
    total = pd.concat(frames)
### plot
#print(total['lon'])
#ATL08_plot.ATL08plot(total, 'IS_all') 

total.to_csv('CSV/' + 'total' +'.csv', index=False)

