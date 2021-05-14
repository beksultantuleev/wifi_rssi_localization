import numpy as np

a = np.array([[5, 0]])
# print(a.shape)
at = np.transpose(a)
# print(a)
a_mult = np.matmul(at, a)
b = np.array([[43]])
# at_b = np.matmul(b, at)
# print(a_mult)
# print(at_b)
# print(a_mult)
# res = np.array([[16, 0],[ 0,  0.]])
# inv_a = np.linalg.inv(a_mult)
# print(inv_a)
# print(res)
# print(a_mult)

def computePosition(a, b):
    # Get 'A_transposed' matrix
    at = np.transpose(a)
    # Get 'A_transposed*A' matrix
    # at_a = np.matmul(at,a)
    a_at = np.matmul(a,at)
    # print(f"this is ata {a_at}")
    # Get '[(A_transposed*A)^-1]' matrix
    inv_a_at = np.linalg.inv(a_at)
    # Get '[A_transposed*B]'
    at_b = np.matmul(at, b)
    # Get '[(A_transposed*A)^-1]*[A_transposed*B]'
    # This holds our position (xn,yn)
    x = np.matmul(at_b, inv_a_at)
    return x

print(computePosition(a, b))

