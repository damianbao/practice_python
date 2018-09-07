# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:00:53 2018

@author: brad
"""

import numpy as np

grid1 = np.array ([[1,0,0,1,1],[0,0,1,0,1]])

grid2 = np.ones ((2, 5), dtype = np.int64)

grid3 = np.full((3,3), '_')

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

for c in range(a.shape[1]):
    print (sum (a[:,c]))
    
np.arange(4)