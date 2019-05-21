import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(-100,100,200)
y = np.linspace(0,0,200)
for i in range(len(x)):
    if x[i] < 0:
        y[i] = -(x[i] ** 2)
    else:
        y[i] = x[i]**2
plt.figure(1,figsize=(4,4))
plt.plot(x, y, label = "hhh")
plt.legend(loc='best')
plt.show()