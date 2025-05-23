def gaussian_elimination(A, b):
    n = len(A)
    # Nối ma trận A và vector b lại
    for i in range(n):
        A[i].append(b[i])

    # Khử Gauss
    for i in range(n):
        # Tìm dòng có phần tử lớn nhất để tránh chia gần 0
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[max_row] = A[max_row], A[i]

        # Chia dòng i cho phần tử A[i][i]
        factor = A[i][i]
        for j in range(i, n + 1):
            A[i][j] /= factor

        # Khử các dòng dưới
        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n + 1):
                A[k][j] -= factor * A[i][j]

    # Thế ngược
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
    return x