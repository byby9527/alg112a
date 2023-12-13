import numpy as np

def step(f, p, k, step_size):
    p1 = p.copy()
    p1[k] += step_size
    return (f(p1) - f(p)) / step_size

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

        if f_new < f_now:
            p = p_new
            print('p=', p, 'f(p)=', f_new)
        else:
            break

def f(p):
    return np.sum(np.array(p)**2)

gradient_descent(f, [2, 1, 3], 1e-2)
