import pandas as pd
import numpy as np
from gurobipy import *

from geodistance import *
from data_structure_Zaman import *

m = Model('Optimize')

X = m.addVars(K, vtype=GRB.BINARY, name='Location Assignment')
Y = m.addVars(J, vtype=GRB.BINARY, name='Served by Source')
Z = m.addVars(J,K, vtype=GRB.BINARY, name='Served by Justice')
W = m.addVars(J,K, vtype=GRB.BINARY, name='Combined')
TL = m.addVars(K, vtype=GRB.INTEGER, name='Truck Load')

m.addConstrs( Y[j] + quicksum(W[j,k] for k in K ) == 1 for j in J) #1st Constraints
m.addConstrs( quicksum(demand[j].sum() * Z[j,k] for j in J) <= 20000 * TL[k] for k in K)
m.addConstrs(W[j,k] == X[k] *Z[j,k] for k in K for j in J)
m.addConstrs(W[j,k] <= X[k] for k in K for j in J)
m.addConstrs(W[j,k] <= Z[j,k] for k in K for j in J)
m.addConstrs(X[k] + Z[j,k] <= W[j,k] + 1 for k in K for j in J )
m.addConstrs(X[k] >= Z[j,k] for k in K for j in J)
m.addConstrs(TL[k] <= 2 for k in K)
            
obj1 = (S/52) * quicksum(X[k] for k in K) #fixed cost
obj2 = quicksum(demand[j,n] * rate_ij[j] * Y[j] * T[j,n]  for n in N for j in J) + quicksum((1 - T[j,n]) * rate_ij_min[j] * Y[j] for n in N for j in J)   #from i to j
obj3 = quicksum(rate_per_mile[k] * dist_ik[k] * X[k] * TL[k] for k in K) + quicksum(shipment[j] * handling_cost[k] * W[j,k] for k in K for j in J) # from i to k
obj4 = quicksum(demand[j,n] * rate_kj[j,k] * W[j,k] * T2[j,n] for n in N for k in K for j in J) + quicksum((1 - T2[j,n]) * rate_kj_min[j,k] * W[j,k] for n in N for k in K for j in J) 

obj = obj1 + obj2 + obj3 + obj4

#obj =  obj2
m.params.timelimit= 5
m.setObjective(obj,GRB.MINIMIZE)
m.update()
m.optimize()