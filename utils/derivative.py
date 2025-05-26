import numpy as np

# Hàm tính đạo hàm của spline bậc ba tại các điểm x
def spline_derivative_at_points(x, b, c, d):
    n = len(x)
    dy = np.zeros(n)
    for i in range(n-1):
        dx = 0  # đạo hàm tại điểm x[i], dx = 0
        dy[i] = b[i] + 2*c[i]*dx + 3*d[i]*dx**2  # = b[i]
    dy[-1] = dy[-2]  # gán đạo hàm điểm cuối giống điểm liền trước (hoặc tùy cách xử lý)
    return dy