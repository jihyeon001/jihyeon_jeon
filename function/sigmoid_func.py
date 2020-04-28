import numpy as np
import matplotlib.pylab as plt
def sigmoid(x):
    return 1 / (1 + np.exp(-x)) 
x = np.array([-1.0, 1.0, 2.0])
y = sigmoid(x)
x = np.arange(-10, 10, 0.1) # -10 ~ 10 까지, 증가값이 0.1인 배열 생성
 
y = sigmoid(x)

plt.plot(x,y)
plt.ylim(-0.1, 1.1)            # y 축 범위 지정
plt.show()
