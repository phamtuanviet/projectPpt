
import numpy as np
import pandas as pd
import argparse
import os
from data.data import save_stock_data_to_csv
from utils.interpolation import cubic_spline_coefficients, spline_evaluate
from utils.derivative import spline_derivative_at_points
from visualization.plot import plot_all



def main():
    parser = argparse.ArgumentParser(description="Spline interpolation on stock data")
    parser.add_argument("csv_file", type=str, help="Path to the CSV file (must include 'Close' column)")
    args = parser.parse_args()

    
    # Ensure the CSV file is in the 'data/csv' directory
    csv_path = os.path.join("data", "csv", args.csv_file)
    # Load data from the provided CSV file
    df = pd.read_csv(csv_path)
    df = df.dropna()
    df = df.reset_index(drop=True)

    y = df['Close'].astype(float).values
    x = np.arange(len(y))

    # Interpolation (custom implementation)
    x_spline = np.linspace(x[0], x[-1], 500)
    b, c, d = cubic_spline_coefficients(x, y)
    y_spline = spline_evaluate(x, y, b, c, d, x_spline)
    dy = spline_derivative_at_points(x, b, c, d)

    extrapolation_range = 10

    # Visualization
    plot_all(x, y, x_spline, y_spline, dy,extrapolation_range )


if __name__ == "__main__":
    main()
