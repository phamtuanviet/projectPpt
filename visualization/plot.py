import matplotlib.pyplot as plt
import numpy as np
from utils.regression import least_squares_fit, evaluate_polynomial

def plot_all(x, y, x_spline, y_spline,dy,extrapolation_range):

    degrees = [1, 2, 3]
    colors = ['r', 'g', 'b']

    plt.figure(figsize=(12, 6))
        
    plt.plot(x, y, 'o', label='Original Data')
    plt.plot(x_spline, y_spline, '-', label='Spline Interpolation')

    for deg, color in zip(degrees, colors):
        coeffs = least_squares_fit(x, y, degree=deg)
        x_pred = np.linspace(x[0], x[-1] + extrapolation_range, 100)
        y_pred = evaluate_polynomial(coeffs, x_pred)
        plt.plot(x_pred, y_pred, label=f'Polynomial degree {deg}', color=color)

    u = np.zeros_like(dy)
    plt.quiver(x, y, u, dy, angles='xy', scale_units='xy', scale=1, color='gray', label='Estimated Derivative')
    plt.legend()
    plt.xlabel("Time Index")
    plt.ylabel("Stock Price")
    plt.title("Stock Price Forecast with Interpolation and Regression")
    plt.grid(True)
    plt.show()