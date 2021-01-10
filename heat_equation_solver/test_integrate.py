from sympy import *
from sympy.integrals.intpoly import *
import numpy as np
from matplotlib import pyplot as plt
x = Symbol('x')
y = Symbol('y')
t = Symbol('t')

x_ = Symbol('x_')
y_ = Symbol('y_')
t_ = Symbol('t_')

del_x = x - x_
k = 1
# quad = Polygon((0, 0), (0, 1), (1, 1), (1, 0))
green = Heaviside(t - t_) * sqrt(4 * pi * k * (t - t_)) * exp(-((x - x_)**2 + (y - y_)**2)/(4 * k * (t - t_)))

# polytope_integrate(quad, exp((x)**2 + (y)**2))

steps_number = 11
h = 1/(steps_number-1)
space = np.linspace(0, 1, steps_number)


def integrate_by(expr, var):
    out = 0
    for i in range(1, steps_number):
        out += expr.subs(var, space[i])*h
    return out


def integrate_in_cube(expr):
    out = integrate_by(expr, x_)
    out = integrate_by(out, y_)
    out = integrate_by(out, t_)
    return out


y_infinity = integrate_in_cube(green) * (x**2 + y**2)
# print(y_infinity.subs(t, 1))
# plotting.plot3d(y_infinity.subs(t, 1))
