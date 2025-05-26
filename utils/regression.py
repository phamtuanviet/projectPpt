import numpy as np
from utils.gaussian import gaussian_elimination

def least_squares_fit(x, y, degree):
    n = len(x)
    # Bước 1: Tạo ma trận A với A[i][j] = x[i] ** j
    A = []
    for i in range(n):
        row = []
        for j in range(degree + 1):
            row.append(x[i] ** j)
        A.append(row)

    # Bước 2: Tính ma trận chuyển vị của A (A^T)
    AT = []
    for j in range(degree + 1):
        row = []
        for i in range(n):
            row.append(A[i][j])
        AT.append(row)

    # Bước 3: Tính ma trận hệ số (AT * A)
    ATA = []
    for i in range(degree + 1):
        row = []
        for j in range(degree + 1):
            total = 0
            for k in range(n):
                total += AT[i][k] * A[k][j]
            row.append(total)
        ATA.append(row)

    # Bước 4: Tính vector vế phải (AT * y)
    ATy = []
    for i in range(degree + 1):
        total = 0
        for k in range(n):
            total += AT[i][k] * y[k]
        ATy.append(total)

    # Bước 5: Giải hệ phương trình tuyến tính ATA * coeffs = ATy
    coeffs = gaussian_elimination(ATA, ATy)

    return coeffs

# Tính giá trị của đa thức tại điểm x
def evaluate_polynomial(coeffs, x):
    result = 0
    for i in range(len(coeffs)):
        result += coeffs[i] * (x ** i)
    return result