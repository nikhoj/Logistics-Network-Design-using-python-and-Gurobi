import pandas as pd
import numpy as np
from gurobipy import *

from geodistance import *
from data_structure_Zaman import *

m = Model('Optimize')

          

obj = quicksum(demand[j] * USPE_rate[j] for j in J) #from i to j

#obj =  obj2
m.params.timelimit= 5
m.setObjective(obj,GRB.MINIMIZE)
m.update()
m.optimize()