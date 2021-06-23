from y_infinity_module import *
from main_D_funcs import func, map_func, appr

x = Symbol('x')
y = Symbol('y')
t = Symbol('t')

# cond
op_11 = 'diff(f, t).subs([(x, 0), (y, 0), (t, 0)])'
op_21 = '(diff(f, x, 2) + diff(f, y)).subs([(x, 0), (y, 0), (t, 0)])'
op_31 = 'diff(f, x).subs([(x, 0.7), (y, 0), (t, 0)])'
op_41 = 'f.subs([(x, 0), (y, 0), (t, 0)])'
op1 = [op_11, op_21, op_31, op_41]

op_12 = 'diff(f, t).subs([(x, 1), (y, 1), (t, 0)])'
op_22 = '(diff(f, x, 2) + diff(f, y)).subs([(x, 0.5), (y, 1), (t, 0)])'
op_32 = 'diff(f, x).subs([(x, 1), (y, 1), (t, 0)])'
op_42 = 'f.subs([(x, 1), (y, 1), (t, 0)])'

r_11 = 0.5
r_21 = 2.0
r_31 = 0.7
r_41 = 0.0
r1 = [r_11, r_21, r_31, r_41]

r_12 = 0.5
r_22 = 2.0
r_32 = 1.0
r_42 = 2.5
op_matrix = [[op_11], [op_12],
             [op_21], [op_22],
             [op_31], [op_32],
             [op_41], [op_42]]

r_matrix = [[r_11], [r_12],
            [r_21], [r_22],
            [r_31], [r_32],
            [r_41], [r_42]]


class Ygamma(Yoo):

    boundary_cond_op = []
    boundary_cond_right = []

    def __init__(self, boundary_cond_op=op_matrix, boundary_cond_right=r_matrix):
        super().__init__()
        self.boundary_cond_op = map_func(boundary_cond_op)
        self.boundary_cond_right = np.array(boundary_cond_right)

        # this is Yoo expr, it is not init in Yoo to ensure that all values are initialized
        self.find_self()

    def build_a_2(self):
        return np.array(appr(self.boundary_cond_op, self.green))

    def build_right_2(self):
        boundary_cond_to_y_inf = np.array(appr(self.boundary_cond_op, self.expr))
        return self.boundary_cond_right - boundary_cond_to_y_inf
