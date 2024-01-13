import numpy as np
# 定義一步的計算，來計算偏導數
def step(f, p, k, step_size):
    p1 = p.copy()
    p1[k] += step_size
    # 計算偏導數
    return (f(p1) - f(p)) / step_size
# 計算梯度
def grad(f, p):
    gp = np.zeros_like(p)
    for k in range(len(p)):
        gp[k] = step(f, p, k, 1e-2)
    return gp

def gradient_descent(f, p, step_size):
    while True:
        f_now = f(p)
        gp = grad(f, p)
        p_new = p - gp * step_size
        f_new = f(p_new)
# 如果新的函數值比當前函數值小，則更新參數並顯示
        if f_new < f_now:
            p = p_new
            print('p=', p, 'f(p)=', f_new)
        else:
            # 若不再改善，則停止迭代
            break

def f(p):
    return np.sum(np.array(p)**2)
# 初始位置及學習率
gradient_descent(f, [2, 1, 3], 1e-2)
