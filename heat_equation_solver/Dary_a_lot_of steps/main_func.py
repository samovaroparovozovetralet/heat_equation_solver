# main class func for MM lab № 4
# author: Alexander Krysynskyi
# release date: Nov 23, 2020
# version: alpha 0.2

from sympy import *
import numpy as np

# basic parameters set
# TO DO: implement this as interface
x = Symbol('x')
y = Symbol('y')
t = Symbol('t')

x_ = Symbol('x_')
y_ = Symbol('y_')
t_ = Symbol('t_')

k = 1
# TO DO: should be function of 3 var not 6
# to integrate this about t` for example, subs method should be used
# smth like: .subs(green, (t, t-t_))
green_default = Heaviside(t - t_) * sqrt(4 * pi * k * (t - t_)) * exp(
    -((x - x_) ** 2 + (y - y_) ** 2) / (4 * k * (t - t_)))
operator_default = lambda f: diff(f, t) - k * (diff(f, x, 2) + diff(f, y, 2))
default_variables = [x, y, t]


class MainFunc:
    var_list = []  # t better be the last variable in list for better experience
    var_list_ = []  # t`, x`, y`  etc. t`
    green = 0
    operator = lambda f: 0
    expr = 0
    integration_steps_default = 5
    h = 1 / (integration_steps_default - 1)
    right = 1  # u func(right expression)

    #   method to build t`, x`, y` etc from list of variable t, x, y etc
    #   see sympy.symbols documentation to understand how it works
    def build_list_(self, var_list):
        phrase = var_list[0].name + '_'
        for i in range(1, len(var_list)):
            phrase += ' ' + var_list[i].name + '_'
        return symbols(phrase)

    def __init__(self, green=green_default, var_list=default_variables, operator=operator_default):
        self.green = green
        self.operator = operator
        self.var_list = var_list
        self.var_list_ = self.build_list_(var_list)

    def find_green(self):
        # TO DO
        print("NOT FOUND")

    def integrate_by(self, func, variable, int_start, int_finish, steps=integration_steps_default):
        out = 0
        space = np.linspace(int_start + self.h/2, int_finish - self.h/2, steps)
        for i in range(0, steps):
            out += func.subs(variable, space[i]) * self.h
        return out

    def integrate_in_cube(self, func, var_list, start_list, finish_list, steps=integration_steps_default):
        out = self.integrate_by(func, var_list[0], start_list[0], finish_list[0])
        for i in range(1, len(var_list)):
            out = self.integrate_by(out, var_list[i], start_list[i], finish_list[i], steps)
        return out
