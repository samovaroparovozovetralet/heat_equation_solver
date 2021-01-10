import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
from scipy.linalg import pinv, det
from itertools import chain, starmap
from sympy import *

x = Symbol('x')
y = Symbol('y')
t = Symbol('t')

class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)
        self._entry = {}
        self.rows = rows
        self.columns = columns

        vcmd = (self.register(self._validate), "%P")

        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e

        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)

        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, P):
        return True

class Example(tk.Frame):
    def __init__(self, parent, n, m):
        tk.Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, n, m)
        self.submit = tk.Button(self, text="Розв'язати", command=self.on_submit)
        self.table.pack(side="top", fill="both", expand=True)
        self.submit.pack(side="bottom")

    def on_submit(self):
        matrix = self.table.get()
        main(matrix)

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

def tab(A_func, space):
    return np.array([appr(A_func, val) for val in space])

#-----------------------------------------------------------------------------------------------------------------------

def main(A0):

    T = 10
    step = T / 1000
    space = np.linspace(0, T, 1000)
    A0 = np.array(A0)

    A_tx = A0[:, :-1].tolist()
    b = A0[:, -1].astype(float)
    print(b)
    m = len(A_tx)
    n = len(A_tx[0])
    v = np.zeros(n)
    A_func = map_func(A_tx)
    print(A_func)
    A = tab(A_func, space)

    p1 = (A @ A.transpose((0, 2, 1))).sum(axis=0) * step     #~integral
    Av = (A @ v).sum(axis=0) * step      #~integral
    x = A.transpose((0, 2, 1)) @ pinv(p1) @ b + v - A.transpose((0, 2, 1)) @ pinv(p1) @ Av
    epsylon = b.T @ b - b.T @ p1 @ pinv(p1) @ b

    if (det((A.transpose((0, 2, 1)) @ A).sum(axis=0))>0):
        print('детермінований')
    else:
        print('не детермінований')
    print('Похибка:', epsylon)

    if n == 1:
        fig, ax = plt.subplots()
        ax.plot(space, x)
        ax.set_xlabel('t')
        ax.set_ylabel('x_1')

    if n == 2:
        ax = plt.gca(projection='3d')
        ax.plot(space, x[:, 0], x[:, 1])
        ax.set_xlabel('t')
        ax.set_ylabel('x_1')
        ax.set_zlabel('x_2')
        plt.tight_layout()

    plt.show()
