#!/usr/bin/env python
# coding: utf-8


import icepyx as ipx
import os

###  need h canopy , lat , lon
import h5py
#read data
path_root = 'C:/Users/xiongl21/WorkingFolder/Postdoc/Icesat2/MyTutorial/Test'
pattern = "processed_ATL{product:2}_{datetime:%Y%m%d%H%M%S}_{rgt:4}{cycle:2}{orbitsegment:2}_{version:3}_{revision:2}.h5"
reader = ipx.Read(path_root, "ATL08", pattern) # or ipx.Read(filepath, "ATLXX") if your filenames match the default pattern

#h_canopy
#
reader.vars.append(var_list=["latitude", "longitude"])
print(reader.vars.wanted)

ds = reader.load()
print(ds)


#filename=reader._filelist[1]
#filename='c:\\Users\\xiongl21\\WorkingFolder\\Postdoc\\Icesat2\\MyTutorial\\processed_ATL06_20190225121032_09020203_005_01.h5'
#with h5py.File(filename, "r") as f:
#    # List all groups
#    print("Keys: %s" % f.keys())
    #gt1r
    #a_group_key = list(f.keys())[2]
    #Get the data
    #data = list(f[a_group_key])
    #print(data)
     #decode a bytes into a str.
    #lat= f[a_group_key]['land_ice_segments/latitude'][:]
    #print(lat)
    #lon= f[a_group_key]['land_ice_segments/longitude'][:]
    #h= f[a_group_key]['land_ice_segments/h_li'][:]





