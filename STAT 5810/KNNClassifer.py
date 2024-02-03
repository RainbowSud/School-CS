import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv('data_seed.dat', header=None, delimiter ="\t")
data.columns = ["Area A",
                "Perimeter P",
                "Compactness C",
                "Length of Kernel",
                "Width of Kernel",
                "Asymmetry Coefficient",
                "Length of Kernel Groove",
                "Classified class number",]

plt.style.use('seaborn')
plt.figure(figsize = (10,10))
plt.scatter(X[:,0], X[:,1], c=y, marker = "*", s=100, edgecolors = 'black')
plt.show()