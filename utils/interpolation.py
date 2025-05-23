import numpy as np

def custom_cubic_spline(x, y, x_new):
    n = len(x)
    h = np.diff(x)
    alpha = [0] + [3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1]) for i in range(1, n - 1)]

    # Khởi tạo hệ phương trình
    l = np.ones(n)
    mu = np.zeros(n)
    z = np.zeros(n)
    l[0] = 1

    for i in range(1, n - 1):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

    b = np.zeros(n - 1)
    c = np.zeros(n)
    d = np.zeros(n - 1)

    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (y[j+1] - y[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])

    def spline_func(xi):
        for i in range(n - 1):
            if x[i] <= xi <= x[i+1]:
                dx = xi - x[i]
                return y[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
        return y[-1]

    y_new = np.array([spline_func(xi) for xi in x_new])
    return y_new
