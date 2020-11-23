import numpy as np
import pandas as pd
from geopy.distance import geodesic

data = pd.read_excel('zip_us.xlsx', header = None, index = None)
us_zip = np.array(data.iloc[:,0]).flatten()
latitude = np.array(data.iloc[:,4]).flatten()
longitude = np.array(data.iloc[:,5]).flatten()

zip_data = np.vstack((us_zip,latitude))
zip_data = np.vstack((zip_data,longitude)).transpose()

sales_data = pd.read_excel('Sales Data.xlsx')
distributors = np.unique(np.array(sales_data.iloc[:,0]))

zip_roi = np.zeros((43,3))
indx = 0
for d in distributors:
    for z in zip_data:
        if d == z[0]:
            zip_roi[indx, 0] = d
            zip_roi[indx, 1] = z[1]
            zip_roi[indx, 2] = z[2]
            indx += 1
            
zip_facility = np.zeros((8,3))
zip_facility[:,0] = np.array([15238,91789,97420,89029,83263,86045,95687,99362] )

indx = 0
for d in zip_facility[:,0]:
    for z in zip_data:
        if d == z[0]:
            zip_facility[indx, 0] = d
            zip_facility[indx, 1] = z[1]
            zip_facility[indx, 2] = z[2]
            indx += 1

dist_source = np.zeros((43,1))
indx = 0
for d in zip_roi:
     loc = (d[1], d[2])
     source = (zip_facility[0,1], zip_facility[0,2])
     dist_source[indx] = geodesic(source, loc).miles
     indx += 1
     
dist_kj = np.zeros((43,7))
i = -1
for d in zip_roi:
    i += 1
    j = 0
    for k in zip_facility[1:]:
        source = (k[1], k[2])
        loc = (d[1], d[2]) 
        dist_kj[i,j] = geodesic(source, loc).miles
    
        j += 1
    
dist_ij = dist_source.flatten()    

dist_ik = np.zeros((7,1))
indx = 0

for k in zip_facility[1:]:
    loc = (k[1], k[2])
    source = (zip_facility[0,1], zip_facility[0,2])
    dist_ik[indx] = geodesic(source, loc).miles
    
    indx += 1

dist_ik = dist_ik.flatten()       
