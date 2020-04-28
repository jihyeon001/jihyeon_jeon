import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0,x)   # numpy의 브로드캐스트

x = np.arange(-10, 10, 0.1) #-10 ~ 10 까지, 증가값이 0.1인 배열 생성
y = relu(x)

plt.plot(x,y)
plt.ylim(-0.1, 10.1)                  # y 축 범위 지정
plt.show()
