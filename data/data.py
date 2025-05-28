import yfinance as yf
import pandas as pd
import os

def save_stock_data_to_csv(ticker: str, start: str, end: str):
    data = yf.download(ticker, start=start, end=end)

    # Chỉ giữ lại cột Date và Close
    df = data[['Close']].copy()

    # Di chuyển chỉ mục (Date) vào thành một cột thông thường,
    df.reset_index(inplace=True)

    # Định dạng lại ngày
    start_fmt = start.replace('-', '')
    end_fmt = end.replace('-', '')

    # Tạo đường dẫn thư mục và tên file
    folder_path = "data/csv"
    os.makedirs(folder_path, exist_ok=True)  # Tạo thư mục nếu chưa có

    filename = f"{ticker.upper()}_{start_fmt}_{end_fmt}.csv"
    filepath = os.path.join(folder_path, filename)

    # Lưu ra CSV
    df.to_csv(filepath, index=False)
    print(f"Đã lưu dữ liệu vào {filepath}")
    return filepath

save_stock_data_to_csv(
    ticker='NFLX',
    start='2022-05-01',
    end='2024-05-01'
)


save_stock_data_to_csv(
    ticker='TSLA',
    start='2024-06-01',
    end='2025-05-28'
)