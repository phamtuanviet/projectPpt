import numpy as np

# Hàm tính hệ số của spline bậc ba
# Dựa trên thuật toán giải hệ phương trình tuyến tính
def cubic_spline_coefficients(x, y):
    n = len(x)
    h = np.diff(x)

    # Tính toán hệ số alpha
    alpha = [0] + [3 * ((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1]) for i in range(1, n-1)]

    # Tạo ma trận hệ phương trình
    # và vector hệ số
    l = np.ones(n)
    mu = np.zeros(n)
    z = np.zeros(n)

    for i in range(1, n-1):
        l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i]

    b = np.zeros(n-1)
    c = np.zeros(n)
    d = np.zeros(n-1)

    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = (y[j+1] - y[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
        d[j] = (c[j+1] - c[j])/(3*h[j])

    return b, c, d

# Hàm đánh giá giá trị của spline tại các điểm mới
# x_new là mảng các điểm cần đánh giá
def spline_evaluate(x, y, b, c, d, x_new):
    n = len(x)
    y_new = np.zeros_like(x_new)
    for idx, xi in enumerate(x_new):
        # tìm đoạn spline chứa xi
        i = np.searchsorted(x, xi) - 1
        if i < 0:
            i = 0
        elif i >= n-1:
            i = n-2
        dx = xi - x[i]
        y_new[idx] = y[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
    return y_new