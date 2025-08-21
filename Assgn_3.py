# Assignment_3:LU Decomposition
# Name: Roshan Yadav
# Roll No: 2311144


from Func_lib_for_assgn_3 import *

# Question 1: LU Decomposition using Doolittle method
print("Question 1: LU Decomposition using Doolittle method")

# Read matrix A from file
A = read_matrix("A.txt")


# Get LU decomposition
result = LU_decomposition(A)

print("\nLU Decomposition Result:",result) 

'''Output of question 1: [[1.0, 2.0, 3.0], [3.0, 2.0, 5.0], [2.0, 1.0, 2.0]]'''


# Question 2: Solve linear equations using LU decomposition
print("\nQuestion 2: Solving Linear Equations using LU decomposition")

# Read matrix C and d from file
C = read_matrix("C.txt")
d = read_vector("d.txt")  


# Solve 
solution = solve_linear_equations(C, d)

print("\nSolution vector x:")
for i, val in enumerate(solution):
    print(f"a{i+1} = {round(val, 6)}")

print("\n")

''' Output: Solution vector x:
a1 = -3.158521
a2 = 2.592302
a3 = 6.991849
a4 = -3.461831
a5 = 2.722799
a6 = 1.368153
'''
