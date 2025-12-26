A = [[1,5,8],
     [4,6,9],
     [7,2,5]]
B= [[4,5,8],
    [8,9,1],
    [3,5,8]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
# print(result)
for r in result:
    print(r)


#using numpy
# import numpy as np
# A = np.array([[12, 7, 3],
#               [4, 5, 6],
#               [7, 8, 9]])
# B = np.array([[5, 8, 1],
#               [6, 7, 3],
#               [4, 5, 9]])
# # Matrix multiplication
# result = np.dot(A, B)   # or A @ B
# print(result)


# #### here is the dynamic NumPy version that works for any matrix size (as long as dimensions are compatible):

# import numpy as np

# # Input matrix sizes
# rows_A = int(input("Enter number of rows for Matrix A: "))
# cols_A = int(input("Enter number of columns for Matrix A: "))
# rows_B = int(input("Enter number of rows for Matrix B: "))
# cols_B = int(input("Enter number of columns for Matrix B: "))

# # Check if multiplication is possible
# if cols_A != rows_B:
#     print("Matrix multiplication not possible! Columns of A must equal rows of B.")
# else:
#     print("\nEnter elements of Matrix A:")
#     A = np.array([list(map(int, input().split())) for _ in range(rows_A)])
    
#     print("\nEnter elements of Matrix B:")
#     B = np.array([list(map(int, input().split())) for _ in range(rows_B)])
    
#     # Matrix multiplication
#     result = np.dot(A, B)   # or A @ B
    
#     print("\nResult of Matrix Multiplication:")
#     print(result)
