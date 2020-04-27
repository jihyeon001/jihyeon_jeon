import numpy as np
import matplotlib.pylab as plt
def relu(x):
    return np.maximum(0,x)  # 브로드 캐스팅 적용, 두 원소중 큰 값을 반환

x = np.arange(-10, 10, 0.1)
y = relu(x)
plt.plot(x,y)
plt.ylim(-0.1, 10.1)
plt.show()