# Assignment_3:LU Decomposition
# Name: Roshan Yadav
# Roll No: 2311144


from Func_lib_for_assgn_3 import *


# Question 1:
A= read_matrix('A.txt')
L,U=LU(A)

P=matmul(L,U)

print('A=',A)
print('L=',L)
print('U=',U)
print('L.U=',P)

