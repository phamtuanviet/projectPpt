def finite_difference(y, h=1):
    # Số điểm
    n = len(y)               
    # Tạo danh sách kết quả với n phần tử 0.0
    dy = [0.0] * n          

    # Sai phân tiến cho điểm đầu tiên
    dy[0] = (y[1] - y[0]) / h

    # Sai phân trung tâm cho các điểm giữa
    for i in range(1, n - 1):
        dy[i] = (y[i + 1] - y[i - 1]) / (2 * h)

    # Sai phân lùi cho điểm cuối cùng
    dy[n - 1] = (y[n - 1] - y[n - 2]) / h

    return dy
