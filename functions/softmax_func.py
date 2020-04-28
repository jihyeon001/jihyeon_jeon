import numpy as np
import matplotlib.pylab as plt

def softmax(a):
    exp = np.exp(a)
    sum_exp = np.sum(exp)
    return exp / sum_exp

y = np.array([4, 5.0, 6.0, 7.0, 10.0]) # 입력값
softmaxed = softmax(y)                # softmax 적용값
sum_softmaxed = np.sum(softmaxed)     # softmax 결과의 합 = 1
plt.scatter([1,2,3,4,5], softmaxed)
plt.show()
