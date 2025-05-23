
import numpy as np
import pandas as pd
from utils.interpolation import custom_cubic_spline
from utils.derivative import finite_difference
from visualization.plot import plot_all



def main():
    # Load data (Date, Close)
    df = pd.read_csv("data/stock.csv")
    df = df.dropna()
    df = df.reset_index(drop=True)

    y = df['Close'].values
    x = np.arange(len(y))

    # Interpolation (custom implementation)
    x_spline = np.linspace(x[0], x[-1], 500)
    y_spline = custom_cubic_spline(x, y, x_spline)

    extrapolation_range = 10

    # Derivative estimation
    dy = finite_difference(y)

    # Visualization
    plot_all(x, y, x_spline, y_spline, dy,extrapolation_range )


if __name__ == "__main__":
    main()
