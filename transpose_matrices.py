A = [[2,9,7],
     [6,5,8]]
T = [[0,0],
     [0,0],
     [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i] = A[i][j]

for t in T:
    print(t)


# using list comprehension
# A = [[2,9,7],
#      [6,5,8]]
# T= [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
# for i in T:
#     print(i)

#     #chatgpt version
# A = [[2,9,7],
#      [6,5,8]]

# T = [list(row) for row in zip(*A)]

# for row in T:
#     print(row)

