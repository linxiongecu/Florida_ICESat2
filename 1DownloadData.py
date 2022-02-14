#!/usr/bin/env python
# coding: utf-8


import icepyx as ipx
import os

# bounding box
short_name = 'ATL08'
#25.42199024389519, -81.13211593174077
#25.43559779200622, -81.10954091371623
#lower left long lat---right top 
spatial_extent = [-120, 52, -119, 53]
##provide shape file to check.
aoi = '/media/sf_Icesat2/MyTutorial/FloridaMangroveAOI.shp'
date_range = ['2019-08-01','2019-08-28']


# In[8]:
region_a = ipx.Query('ATL08',aoi,['2018-09-01','2022-02-09'],                            start_time='00:00:00', end_time='23:59:59')


#get a list of granule IDs for the available granules
region_a.avail_granules(ids=True)


earthdata_uid = 'hopebear_ecu'
email = 'lxiong2@uh.edu'
region_a.earthdata_login(earthdata_uid, email)

#password:  n5nm_7y%c-3%jWv

# In[12]:


region_a.subsetparams() # subset the data by bounding box

region_a._geom_filepath
# In[13]:


region_a.order_granules()


# In[14]:


#view a short list of order IDs
region_a.granules.orderIDs


# In[15]:


path = '/media/sf_Icesat2/MyTutorial/FloridaData'
region_a.download_granules(path)


# In[2]:


#read data
#path_root = 'c:\\Users\\xiongl21\\WorkingFolder\\Postdoc\\Icesat2\\MyTutorial'
#pattern = "processed_ATL{product:2}_{datetime:%Y%m%d%H%M%S}_{rgt:4}{cycle:2}{orbitsegment:2}_{version:3}_{revision:2}.h5"
#reader = ipx.Read(path_root, "ATL06", pattern) # or ipx.Read(filepath, "ATLXX") if your filenames match the default pattern


#In[4]:


#reader._filelist[1]
#reader.vars.avail()


# In[4]:


#reader.vars.remove(all=True)
#reader.vars.append(beam_list=['gt2l'], var_list=['latitude', 'longitude'])
#reader.vars.append(beam_list=['gt1l', 'gt3r'], var_list=['h_li', "latitude", "longitude"])
#reader.vars.remove(var_list=['rgt','cycle_number'])
#reader.vars.wanted


# In[2]:


###ds = reader.load()   crash
#import h5py
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





