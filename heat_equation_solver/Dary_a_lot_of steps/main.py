from sympy import *
# from y_infinity_module import *
from y_0_module import *
from y_gamma_module import Ygamma
# from scipy.linalg import pinv
from gui import *
from solver import solve
from operator_point_parser import build_operator_col

green = list_1[1]
operator = list_1[0]
r_0 = int(list_1[7])
print(r_0)
r_gam = int(list_1[8])
print(list_1)
print(list_2)
print(list_3)
l = int(list_1[9])
operator_point = build_operator_col(list_2[0:r_0], list_2[r_0 + r_gam:l + r_0 + r_gam], 'point')
operator_boundary = build_operator_col(list_2[r_0:r_0+r_gam], list_2[l + r_0 + r_gam:], 'boundary')
right_point = []
right_boundary = []
for i in range(r_0*l):
    zubra = [float(list_3[i])]
    right_point.append(zubra)

for i in range(r_0*l, r_0*l + r_gam*l):
    zubra = [float(list_3[i])]
    right_boundary.append(zubra)


y_0 = Y0(point_cond_op=operator_point, point_cond_right=right_point)
y_gamma = Ygamma(boundary_cond_op=operator_boundary, boundary_cond_right=right_boundary)
# y_0 = Y0()
# y_gamma = Ygamma()
p, b, u_0, u_gamma, err = solve(y_0, y_gamma)
y_0_expr = y_0.integrate_in_cube(y_0.green * u_0, [x_, y_, t_], [0, 0, -10], [1, 1, 0], 5)
y_gamma_expr = y_gamma.integrate_in_cube(y_gamma.green * u_gamma, [x_, y_, t_], [-10, -10, 0], [10, 10, 1], 5) \
               - y_gamma.integrate_in_cube(y_gamma.green * u_gamma, [x_, y_, t_], [0, 0, 0], [1, 1, 1], 3)
y_sum = y_0.expr + y_0_expr + y_gamma_expr
print(y_0_expr)
print(y_gamma_expr)
print(y_0.expr)
print(y_sum)


# plotting.plot3d(y_sum.subs(t, 0.11), (x, 0, 1), (y, 0, 1))
if y_0_expr.subs(t, 0.11) != 0:
    plotting.plot3d(y_0_expr.subs(t, 0.11), (x, 0, 1), (y, 0, 1))

# plotting.plot3d(y_gamma_expr.subs(t, 0.11), (x, 0, 1), (y, 0, 1))

# plotting.plot3d(y_0.expr.subs(t, 0.11), (x, 0, 1), (y, 0, 1))

# plotting.plot3d(y_sum.subs(t, 0.51), (x, 0, 1), (y, 0, 1))

# plotting.plot3d(y_0_expr.subs(t, 0.51), (x, 0, 1), (y, 0, 1))
if y_gamma_expr.subs(t, 0.51) != 0:
    plotting.plot3d(y_gamma_expr.subs(t, 0.51), (x, 0, 1), (y, 0, 1))

# plotting.plot3d(y_0.expr.subs(t, 0.51), (x, 0, 1), (y, 0, 1))

plotting.plot3d(y_sum.subs(t, 0.91), (x, 0, 1), (y, 0, 1))

plotting.plot3d(y_0_expr.subs(t, 0.91), (x, 0, 1), (y, 0, 1))
if y_gamma_expr.subs(t, 0.91) != 0:
    plotting.plot3d(y_gamma_expr.subs(t, 0.91), (x, 0, 1), (y, 0, 1))

plotting.plot3d(y_0.expr.subs(t, 0.91), (x, 0, 1), (y, 0, 1))
