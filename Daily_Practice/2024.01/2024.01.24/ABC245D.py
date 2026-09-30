import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]

A_eq = np.poly1d(A)
C_eq = np.poly1d(C)

# Perform polynomial division
quotient, remainder = np.polydiv(C_eq, A_eq)

# Extract coefficients of the quotient
quotient_coefficients = quotient.coefficients

# print(quotient_coefficients)
ans = []

for num in quotient_coefficients[::-1]:
    ans.append(int(num))


print(*ans)
