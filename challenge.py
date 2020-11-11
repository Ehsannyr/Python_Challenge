###########################
# Author: Ehsan Nayernia  #
# Pyhton version: 3.8     #
###########################

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

## calculation section
data = pd.read_csv('results.csv')

sp = data.loc[248,:]

for c in sp.values:
    vec = sp[7].split(' ')
    n_vec = np.array(vec)
    
flt = n_vec.astype(np.float)

avg = np.average(flt)
print('mean is: ', avg)

## plot section
plt.plot(flt, 'r', avg, 'g^')
plt.suptitle('vector Plot')
plt.xlabel('value')
plt.ylabel('number')

plt.savefig('out.png', format='png', dpi=160)   # dpi to resolution convert

plt.show()
