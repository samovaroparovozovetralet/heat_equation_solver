import numpy as np
from sympy import *

x = Symbol('x')
y = Symbol('y')
t = Symbol('t')


def func(s, var='f'):
    return eval(f'lambda {var}: {s}')

def map_func(A_tx):
    if isinstance(A_tx[0], list):
        A_func = []
        for row in A_tx:
            row_func = list(map(lambda s: func(s), row))
            A_func.append(row_func)
        return A_func
    else:
        return list(map(lambda s: func(s), A_tx))

def appr(A_func, val):
    if isinstance(A_func[0], list):
        A_tab = []
        for row in A_func:
            row_tab = list(map(lambda f: f(val), row))
            A_tab.append(row_tab)
        return np.array(A_tab)
    else:
        return np.array(list(map(lambda f: f(val), A_func)))
