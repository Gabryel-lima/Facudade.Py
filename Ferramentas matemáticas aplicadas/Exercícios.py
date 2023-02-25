import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import *
from pulp import *
from scipy.interpolate import *


A=np.array([[4,-3,1],[1,1,3],[2,3,-4]])
b=np.array([[15],[27],[31]])
X=np.linalg.solve(A,b)
print(X)




