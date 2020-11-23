import pandas as pd
import numpy as np


#read the Datafile

file = 'Data_sheets.xlsx'
data = pd.read_excel(file, header =None, index = None , sheet_name= 'demand')
demand = np.array(data).transpose()
theta1 = 10.715
theta2 = 11
T = demand.copy()
T2 = demand.copy()
for i in range(T.shape[0]):
    for j in range(T.shape[1]):
        if T[i,j] < theta1 and T[i,j] != 0:
            T[i,j] = 0
        elif T[i,j] == 0:
            T[i,j] = 1
        else:
            T[i,j] = 1
        
        if T2[i,j] < theta2 and T2[i,j] != 0:      
            T2[i,j] = 0
        elif T2[i,j] == 0:
            T2[i,j] = 1
        else:
            T2[i,j] = 1
        

data = pd.read_excel(file, header =None, index = None , sheet_name= 'rkj')
USPE_rate_from_justice = np.array(data)
rate_kj = USPE_rate_from_justice
rate_kj_min = rate_kj.copy() 
for i in range(rate_kj_min.shape[0]):
    for j in range(rate_kj_min.shape[1]):
        if rate_kj_min[i,j] == .33:
            rate_kj_min[i,j] = 4.20
        elif rate_kj_min[i,j] == .37:
            rate_kj_min[i,j] = 4.65
        elif rate_kj_min[i,j] == .41:
            rate_kj_min[i,j] = 5.00
        elif rate_kj_min[i,j] == .46:
            rate_kj_min[i,j] = 5.4
        elif rate_kj_min[i,j] == .5:
            rate_kj_min[i,j] = 5.85
        elif rate_kj_min[i,j] == .54:
            rate_kj_min[i,j] = 6.10        
        elif rate_kj_min[i,j] == .59:
            rate_kj_min[i,j] = 6.45
    

data = pd.read_excel(file, header =None, index = None , sheet_name= 'rj1')
rate_ij = np.array(data).flatten()
rate_ij_min = rate_ij.copy()
for i in range(len(rate_ij_min)):
    if rate_ij_min[i] == .58:
        rate_ij_min[i] = 6.3
    else:
        rate_ij_min[i] = 7.4

#data = pd.read_excel(file, header =None, index = None , sheet_name= 'dik')
#distance = np.array(data).flatten()

data = pd.read_excel(file, header =None, index = None , sheet_name= 'rk')
rate_per_mile = np.array(data).flatten()
rate_per_mile = rate_per_mile/ 2

data = pd.read_excel(file, header =None, index = None , sheet_name= 'hk')
handling_cost = np.array(data).flatten()

data = pd.read_excel(file, header =None, index = None , sheet_name= 'nj')
shipment = np.array(data).flatten()


S = 40000
K = np.arange(0,7,1)
I = np.arange(0,1,1)
J = np.arange(0,43,1)
N = np.arange(0,39,1)






