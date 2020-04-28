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

x2 = np.arange(-5.0, 5.0, 0.1)  #-5 ~ 5까지, 증가값이 0.1인 배열 생성
y = step_function(x2)
plt.plot(x2,y)
plt.ylim(-0.1,1.1)                     # y 축 범위 지정
plt.show()
