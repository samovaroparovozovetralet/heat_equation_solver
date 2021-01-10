# from sympy import *
# from main_D_funcs import appr, map_func
# import numpy as np
from y_0_module import *
from y_gamma_module import Ygamma
from scipy.linalg import pinv


def integrate_in_s_0(matrix, y_0):
    rows, cols = matrix.shape
    out = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            out[i][j] = y_0.integrate_in_cube(matrix[i][j], [x_, y_, t_], [0, 0, -10], [1, 1, 0], 5)
    return out


def integrate_in_s_gamma(matrix, y_gamma):
    rows, cols = matrix.shape
    out = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            out[i][j] = y_gamma.integrate_in_cube(matrix[i][j], [x_, y_, t_], [-10, -10, 0], [10, 10, 1], 5) \
                      - y_gamma.integrate_in_cube(matrix[i][j], [x_, y_, t_], [0, 0, 0], [1, 1, 1], 3)
    return out


def solve(y_0, y_gamma):
    a_1 = y_0.build_a_1()
    a_2 = y_gamma.build_a_2()
    b_1 = y_0.build_right_1()
    b_2 = y_gamma.build_right_2()
    b = np.append(b_1, b_2)
    a_1_1 = a_1 @ a_1.T
    a_1_2 = a_1 @ a_2.T
    a_2_1 = a_2 @ a_1.T
    a_2_2 = a_2 @ a_2.T
    p_11 = integrate_in_s_0(a_1_1, y_0) + integrate_in_s_gamma(a_1_1, y_gamma)
    p_12 = integrate_in_s_0(a_1_2, y_0) + integrate_in_s_gamma(a_1_2, y_gamma)
    p_21 = integrate_in_s_0(a_2_1, y_0) + integrate_in_s_gamma(a_2_1, y_gamma)
    p_22 = integrate_in_s_0(a_2_2, y_0) + integrate_in_s_gamma(a_2_2, y_gamma)
    p1 = np.append(p_11, p_21, axis=0)
    p2 = np.append(p_12, p_22, axis=0)
    p = np.append(p1, p2, axis=1)
    # print(p.shape)

    p_inv = pinv(p)
    a_0 = np.append(a_1.T, a_2.T, axis=-1)
    a_gamma = np.append(a_1.T, a_2.T, axis=-1)
    # print(b.shape)
    # print(a_0.shape)
    # print(a_gamma.shape)
    u_0 = a_0 @ p_inv @ b
    u_gamma = a_gamma @ p_inv @ b
    # print(u_0.shape)
    # print(u_gamma.shape)
    err = b @ b.T - b @ p @ p_inv @ b.T
    print('Похибка = ', err.evalf())
    return p, b, u_0[0], u_gamma[0], err

