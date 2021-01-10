from sympy import *


def build_point_cond_single(operator, point):
    return operator + '.subs([(t, 0), ' + point + '])'


def build_boundary_cond_single(operator, point):
    return operator + '.subs([' + point + '])'


def build_operator_col(ops, points, name):
    r = len(ops)
    l = len(points)
    operator_col = []
    for i in range(r):
        for j in range(l):
            if name == 'point':
                operator_col.append([build_point_cond_single(ops[i], points[j])])
            if name == 'boundary':
                operator_col.append([build_boundary_cond_single(ops[i], points[j])])
    return operator_col

