#This script contains functions for LU decomposition and solving linear equations using the LU decomposition method.
# # Name: Roshan Yadav
# Roll No: 2311144

from typing import List, Union

def read_matrix(filename):

    with open( filename , 'r' ) as f :
        matrix =[]
        for line in f :
            # Convert each line into a list of floats
            row = [ float(num) for num in line.strip().split() ]
            matrix.append(row)
    return matrix

def matmul(M: List[List[float]], N: List[List[float]]) -> Union[str, List[List[float]]]:
    """
    Perform matrix multiplication of two matrices M and N.
    
    Args:
        M (List[List[float]]): First matrix (m*k)
        N (List[List[float]]): Second matrix (k*n)
        
    Returns:
        Union[str, List[List[float]]]: Result matrix or error message
        
    Note:
        For matrix multiplication MN to be valid:
        - Number of columns in M must equal number of rows in N
        - Result will be an (m*n) matrix
    """
    if not M or not N or not M[0] or not N[0]:
        return "Error: Empty matrices provided"
    
    rows_M, cols_M = len(M), len(M[0])
    rows_N, cols_N = len(N), len(N[0])
    
    # Check if multiplication is possible
    if cols_M != rows_N:
        return f"Error: Cannot multiply {rows_M}*{cols_M} matrix with {rows_N}*{cols_N} matrix"
    
    # Initialize result matrix with zeros
    result = [[0.0 for _ in range(cols_N)] for _ in range(rows_M)]
    
    # Perform matrix multiplication
    for i in range(rows_M):
        for j in range(cols_N):
            for k in range(cols_M):
                result[i][j] += M[i][k] * N[k][j]
    
    return result


def LU(A):
    """
    Perform LU decomposition of matrix A
    using Doolittle.

    """
    n = len(A)
    L=[]
    U=[]
    for i in range(n):
        K=[]
        for j in range(n):
            K.append(0)
        L.append(K)
        U.append(K)
        U[0][i]=A[0][i]

    for j in range(0,n):
        for i in range(1,n):
            if i<j or i==j:
                s=0
                for k in range(1,i):
                    s = s  + (float(L[i][k]))*(float(U[k][j]))
                    print(s)
                L[i][j]= A[i][j] - s
            else:
                pass
    for j in range(0,n):
        for i in range(1,n):
            if i>j:
                s=0
                for k in range(1,j):
                    s = s + (L[i][k])*(U[k][j])
                L[i][j]= (A[i][j] - s)/(U[j][j])
            else:
                pass
        
    return L,U

        


        
    