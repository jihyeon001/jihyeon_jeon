import numpy as np
def numerical_gradient(f,x):     # 편미분 함
    h = 1e-4
    grad = np.zeros_like(x)      # n개의 array로 구성된 변수
    for idx in range(x.size):    # x 개수 만큼 미분을 반복
        tem_val = x[idx]
        x[idx] = tem_val + h
        fxh1 = f(x)
        x[idx] = tem_val - h
        fxh2 = f(x)
        grad[idx] = (fxh1-fxh2)/(2*h)
        x[idx] = tem_val
    return grad
def gradient_descent(f,init_x,relaxation_f,iteration):
    x = init_x
    for i in range(iteration):
        grad = numerical_gradient(f,x)
        x -= relaxation_f*grad
        print(x)
    return x
def function_b(x):
    return (x[0]**2+x[1]**2)
init_x = np.array([-3.0,4.0])
gradient_descent(function_b,init_x,0.1,50)