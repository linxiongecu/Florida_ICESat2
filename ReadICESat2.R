### read icesat2 data
library(hdf5r)

DataDir='C:/Users/xiongl21/WorkingFolder/Postdoc/Icesat2/MyTutorial/FloridaData/'
# output name list
filelist <- Sys.glob(file.path(DataDir, "processed_*"))

filelist
## create data table 
rh.dt<-data.table::data.table()

for(var in 1:length(filelist))
{ 
  
  print(var)

#file = 'data/processed_ATL08_20181017085235_02860107_005_01.h5'
level2a <- hdf5r::H5File$new(filelist[var], mode = 'r')

groups_id<-grep("^gt",gsub("/","", hdf5r::list.groups(level2a, recursive = F)), value = T)

# atl08 data  /gt1l/land_segments/canopy/h_canopy

pb <- utils::txtProgressBar(min = 0, max = length(groups_id), style = 3)
i.s=0
time = level2a[['ancillary_data/data_start_utc']][]
## orbit orientation 
sc_orient = level2a[['orbit_info/sc_orient']][]

for ( i in groups_id){
  i.s<-i.s+1
  utils::setTxtProgressBar(pb, i.s)
  
  beam = i
  # next level 
  level2a_i<-level2a[[i]]
  
  
   if (names(level2a_i)[1] == 'land_segments'){ 
     level2a_i <- level2a_i[['land_segments']]
   }  else {
     next}
  
  ##list attr
  hdf5r::list.datasets(level2a_i)
  
  
  if (any(hdf5r::list.datasets(level2a_i)=="canopy/h_canopy")){
    # record 2D table data.
    
    # if(length(level2a_i[["rh"]]$dims)==2) {
    #   rh=t(level2a_i[["rh"]][,])
    # } else {
    #   rh=t(level2a_i[["rh"]][])
    # }
    # 
    
    
    rhs<-data.table::data.table(
      #beam<-rep(i,length(level2a_i[["shot_number"]][])),
      time,
      beam,
      sc_orient,
      latitude=level2a_i[["latitude"]][],
      longitude=level2a_i[["longitude"]][],
      night_flag=level2a_i[["night_flag"]][],
      h_canopy=level2a_i[["canopy/h_canopy"]][],
      h_canopy_uncertainty = level2a_i[["canopy/h_canopy_uncertainty"]][],
     # degrade_flag=level2a_i[["degrade_flag"]][],
      #quality_flag=level2a_i[["quality_flag"]][],
      #quality_flag=level2a_i[["delta_time"]][],
      #sensitivity=level2a_i[["sensitivity"]][],
      #solar_elevation=level2a_i[["solar_elevation"]][],

     h_te_best_fit=level2a_i[["terrain/h_te_best_fit"]][],
     h_te_uncertainty=level2a_i[["terrain/h_te_uncertainty"]][]
     
     # elev_highestreturn=level2a_i[["elev_highestreturn"]][],
      #elev_lowestmode=level2a_i[["elev_lowestmode"]][],
      #rh)
    )
    rh.dt<-rbind(rh.dt,rhs)
  }
}

colnames(rh.dt)<-c("time","beam","sc_orient","latitude","longitude","night_flag","h_canopy","h_canopy_uncertainty",
                   "h_te_best_fit","h_te_uncertainty")
close(pb)

}

write.csv(rh.dt,'out.csv' , row.names = FALSE)

#return(rh.dt)