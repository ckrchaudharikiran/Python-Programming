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
    for j in range(len(A[0])):
        result[i][j] = A[i][j]+ B[i][j]

for r in result:
    print(r)



#optimized version of code

# A = [[1,5,8],
#      [4,6,9],
#      [7,2,5]]

# B = [[4,5,8],
#      [8,9,1],
#      [3,5,8]]

# # Matrix addition using list comprehension
# result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# for row in result:
#     print(row)
