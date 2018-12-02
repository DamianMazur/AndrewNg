import numpy as np

# matrix (obsolete np.matrix)
A = np.matrix('1 2 3; 4 5 6; 7 8 9; 10 11 12')
print(A)

# vector
v = np.array([1, 2, 3])
print(v)

# dimension of the matrix A
print(A.shape)

# dimension of the vector v
print(v.shape)

# indexing into the 2nd row 3rd column of matrix A
A23 = A.item((1, 2))
print(A23)

# initialize matrix X and Y
X = np.array([[1, 2, 4], [5, 3, 2]], np.int32)
Y = np.array([[1, 3, 4], [1, 1, 1]], np.int32)

# initialize constant s
s = 2

# see how element-wise addition works
add_XY = X + Y
print(add_XY)

# see how element-wise subtraction works
sub_XY = X - Y
print(sub_XY)

# see how scalar multiplication works
mult_Xs = X * s
print(mult_Xs)

# scalar division
div_Xs = X / s
print(div_Xs)

# What happens if we have a matrix + scalar?
add_Xs = X + s
print(add_Xs)

# matrix vector multiplication
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
h = np.array([[1], [1], [1]])
print(h)

Mh = M @ h
print(Mh)


# matrix matrix multiplication
C = np.array([[1, 2], [3, 4], [5, 6]])
D = np.array([[1], [2]])

mult_Cd = C @ D
print(mult_Cd)

# matrix properties (Matrices are not commutative, but are
# associative)

# identity matrix
I = np.eye(2)
print(I)

# transposing matrices
D_trans = D.transpose()
print(D_trans)

# inversing matrices
D_inv = np.linalg.pinv(D)
print(D_inv)

# quiz
u = np.array([[3], [-5], [4]])
k = np.array([[1], [2], [5]])

u_trans = u.transpose()
answer = u_trans @ k
print(answer)