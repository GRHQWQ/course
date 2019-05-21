#from sklearn import preprocessing
from sklearn.preprocessing import scale
import numpy as np 
a = np.array([[13,98,-99],
[87,30,-140],
[-24,80,80]])

print(scale(a))

import matplotlib.pyplot as plt

# print(a[0,:])
# print(a[1,:])
# plt.scatter(a[0,:],a[1,:])

a = [i for i in range(0,1000)]
b = []
for i in a:
    b.append(pow(i,1/2))
plt.scatter(a,b)
plt.show()