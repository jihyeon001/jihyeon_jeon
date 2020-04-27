import numpy as np
import matplotlib.pylab as plt

x = np.array([-1.0, 1.0, 2.0])
print(x) # [-1.  1.  2.]
y = x>0
print(y) # [False  True  True]
z = np.array(x>0, dtype=np.int)
print(z) # [0 1 1]

def step_function(x):
    return np.array(x>0, dtype=np.int)
x2 = np.arange(-5.0, 5.0, 0.1) # 71p 오타
y = step_function(x2)
plt.plot(x2,y)
plt.ylim(-0.1,1.1)
plt.show()