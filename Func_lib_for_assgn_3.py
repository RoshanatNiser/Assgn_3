# Assignment 3: LU Decomposition Functions
# Name: Roshan Yadav
# Roll No: 2311144
# Method Used: Doolittle

def read_matrix(filename):
    with open( filename , 'r' ) as f :
        matrix =[]
        for line in f :
            # Convert each line into a list of floats
            row = [ float(num) for num in line.strip().split() ]
            matrix.append(row)
    return matrix

def read_vector(filename):
    """
    Read a vector from a file (one number per line)
    """
    with open(filename, 'r') as f:
        vector = []
        for line in f:
            vector.append(float(line.strip()))
    return vector

def LU_decomposition(A):
    """
    This function recturns LU decomposition of matrix A using Doolittle method.

    """
    n = len(A)
    
    # Doolittle LU Decomposition Algorithm
    for i in range(n):
        # Calculate U matrix elements (upper triangular)
        for k in range(i, n):
            sum_val = 0
            for j in range(i):
                sum_val += A[i][j] * A[j][k]
            A[i][k] = A[i][k] - sum_val
        
        # Calculate L matrix elements (lower triangular)
        for k in range(i+1, n):
            sum_val = 0
            for j in range(i):
                sum_val += A[k][j] * A[j][i]
            A[k][i] = (A[k][i] - sum_val) / A[i][i]
    
    return A

def solve_linear_equations(A, b):
    """
    This fuction solves system of linear equations using LU decomposition
    with forward-backward substitution.
   
    """
    n = len(A)
    
    # Step 1: Get LU decomposition
    LU_combined = LU_decomposition(A)
    
    # Step 2: Extract L and U matrices from LU
    L = []
    U = []
    for i in range(n):
        L_row = []
        U_row = []
        for j in range(n):
            if i == j:
                L_row.append(1.0)  # Diagonal of L is 1 
                U_row.append(LU_combined[i][j])
            elif i > j:
                L_row.append(LU_combined[i][j])  # Lower triangular
                U_row.append(0.0)
            else:
                L_row.append(0.0)
                U_row.append(LU_combined[i][j])  # Upper triangular
        L.append(L_row)
        U.append(U_row)
    
    # Step 3: Forward Substitution - Solve Ly = b
    y = []
    for i in range(n):
        sum_val = 0
        for j in range(i):
            sum_val += L[i][j] * y[j]
        y.append(b[i] - sum_val)
    
    # Step 4: Backward Substitution - Solve Ux = y
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        sum_val = 0
        for j in range(i+1, n):
            sum_val += U[i][j] * x[j]
        x[i] = (y[i] - sum_val) / U[i][i]
    
    return x
