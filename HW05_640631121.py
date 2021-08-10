# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:30:31 2021

@author: Omen
"""

import numpy as np
from scipy.linalg import solve
A = [[[0.2,0.5],[1,1]],[[0.2,0.5],[1,0]],
     [[0.2,0.5],[0,1]],[[1,0],[1,1]],[[0,1],[1,1]]]
b = [[10,30],[10,0],[10,0],[0,30],[0,30]]
maxx = []
for i in range (5):
    x = solve(A[i],b[i])
    x = x.astype(int)
    constraints = (
        x[0]+x[1] <= 30,
        x[0] >= 0,
        x[1] >= 0,
        0.2*x[0]+0.5*x[1] <=10)
    if all(constraints) :
        C = np.array([3,2])
        Z = np.dot(C,x)
        maxx.append(Z)
        
maximum = max(maxx)
print("""When a box of ice cream is sold, you will get the benefit 
for $2 for vanilla ice cream and $3 for strawberry ice cream""")
print("\nMaximum profit per day of your ice cream is", maximum, "$")