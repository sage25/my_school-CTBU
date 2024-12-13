from sympy import Symbol
from sympy import symbols
from sympy import factor
from sympy import expand
from sympy import simplify
from sympy import solve
from sympy import Derivative
from sympy import pprint
from sympy import sympify
from sympy import Integral
from sympy.core.sympify import SympifyError
import numpy as np


# x = Symbol('x')
# print(x + x + 1)

# x ,y = symbols('x ,y')
# s = x * y + x * y
# print(s)

# x ,y = symbols('x , y')
# equ = x ** 2 - y ** 2
# print(factor(equ))
# equ2 = (x + y)**3
# print(expand(equ2))

# x , y = symbols('x , y')
# equ = x ** 2 + 2*x*y + y ** 2
# res = equ.subs({x:1, y:2})
# print(res)
# equ2 = equ.subs({x:y-1})
# print(equ2)
# print(simplify(equ2))

# x = Symbol('x')
# equ = x * 2 -9
# print(solve(equ))

# x = Symbol('x')
# equ = x ** 2 + 5 * x + 4
# print(solve(equ))
# print(solve(equ,dict=True))

# x ,y = symbols('x ,y')
# equ1 = 2 * x + 3 * y - 6
# equ2 = 3 * x + 2 * y - 12 
# print(solve((equ1, equ2),dict=True))

# t = Symbol('t')
# St = 5*t**2 + 2*t + 8
# Derivative(St ,t)
# d = Derivative(St ,t)
# print(d.doit())
# t1 = Symbol('t1')
# print(d.doit().subs({t:t1}))
# print(d.doit().subs({t:2}))


#################################################
# def derivative(f ,var ,ord):
#     var = Symbol(var)
#     d = Derivative(f, var, ord).doit()
#     pprint(d)

# if __name__ == '__main__':
#     f = input('请输入求导函数')
#     var = input('请输入求导变量')
#     ord = input('请输入求导阶数')

#     try:
#         f = sympify(f)
#     except SympifyError:
#         print("输入无效")
#     else:
#         derivative(f,var,ord)

#################################################
# x ,k = symbols('x, k')
# print(Integral(k*x,x).doit())
# print(Integral(k*x,(x,2,4)).doit())

# a = np.array([4 ,3])
# b = np.array([[4,3]])
# c = np.array([4,3],ndmin=2)
# a1 = a.T
# print(a1)
# b1 = b.T
# print(b1)

# a = np.array([-3,8])
# b = np.array([4,2])
# ab_add = a + b
# # np.add
# a_m_b = a - b 
# # np.aubtract
# b_m_a = b - a
# c = 2*a

# print(f'a + b = {ab_add}')
# print(f'a - b = {a_m_b}')
# print(f'b - a = {b_m_a}')
# print(f'2a = {c}')

# a = np.array([4,3,2])
# b = np.array([5,-2,1])
# a_d_b = np.inner(a,b)
# a_d_b2 = np.dot(a,b)
# a_c_b = np.cross(a,b)
# a_p_b = a * b
# #np.multiply
# print(f'向量内积： {a_d_b}')
# print(f'向量内积： {a_d_b2}')
# print(f'向量外积： {a_c_b}')
# print(f'向量逐项积： {a_p_b}')

# m = np.matrix([[1,2],[3,4]])
# m1 = np.matrix('1 2;3 4')
# m2 = np.array([[1,2],[3,4]])
# print(f'The matrix m is {m}, the shape is {m.shape}')
# print(f'The matrix  m1 is {m1}, the shape {m1.shape}')
# print(f'The matrix m2 is {m2}, the shape is {m2.shape}')

# n = 3
# identity_matrix = np.eye(n)
# #identity_matrix = np.identity(n)
# print(identity_matrix)
# diagonal_elements = np.array([1,2,3])
# diagonal_matrix = np.diag(diagonal_elements)
# print(diagonal_matrix)
# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# main_diagonal = np.diag(matrix)
# print(main_diagonal)
# upper_triangular_matrix = np.triu(diagonal_matrix)
# lower_triangular_matrix = np.tril(diagonal_matrix)
# print(upper_triangular_matrix)
# print(lower_triangular_matrix)

# A = np.matrix([[1,2],[3,4]])
# B = np.matrix([[2,3],[4,5]])
# ab_add = A + B
# a_m_b = A - B 
# b_m_a = B - A
# c = 2*A
# print(f'A + B = {ab_add}')
# print(f'A - B = {a_m_b}')
# print(f'B - A = {b_m_a}')
# print(f'2A = {c}')

# A = np.array([[1,2,3],[4,5,6]])
# print(A.shape)
# B = np.array([[1,2],[3,4],[5,6]])
# print(B.shape)
# A_m_B = np.matmul(A,B)
# print(f'matrix A mulitiply matrix B is {A_m_B}')

A = np.array([[1,2],[3,4]])
B = np.matrix([[1,2],[3,4]])
A_inverse = np.linalg.inv(A)
A_T = A.T
B_inverse = B.I
tr_A = np.trace(A)
det_A = np.linalg.det(A)
print(f'The inverse of A is {A_inverse}')
print(f'The transpose of A is  {A_T}')
print(f'The inverse of B is {B_inverse}')
print(f'The trace of A is {tr_A}')
print(f'The det of A is {det_A}')