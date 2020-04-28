import numpy as np
import matplotlib.pyplot as plt
def binary_step_activate_function(x):
    return np.tanh(x)
    
x = np.arange(-10, 10, 0.1)    #-10 ~ 10 까지, 증가값이 0.1인 배열 생성        
y = binary_step_activate_function(x)
plt.plot(x,y)
plt.show()