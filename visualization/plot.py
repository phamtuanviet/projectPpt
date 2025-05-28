import matplotlib.pyplot as plt
import numpy as np
from utils.regression import least_squares_fit, evaluate_polynomial
from utils.evaluate import evaluate_accuracy

def plot_all(x, y, x_spline, y_spline,dy,extrapolation_range):

    split_idx = int(len(x) * 5 / 6)
    x_train, y_train = x[:split_idx], y[:split_idx]
    x_test,  y_test  = x[split_idx:], y[split_idx:]

    degrees = [1,2,3]  
    colors = ['r', 'g', 'b']

    plt.figure(figsize=(12, 6))
        
    plt.plot(x, y, 'o', label='Original Data')
    plt.plot(x_spline, y_spline, '-', label='Spline Interpolation')

    for deg, color in zip(degrees, colors):
        coeffs = least_squares_fit(x_train, y_train, degree=deg)
        #print(coeffs)
        x_pred_train = np.linspace(x_train[0], x_train[-1], 100)
        y_pred_train = evaluate_polynomial(coeffs, x_pred_train)
        plt.plot(x_pred_train, y_pred_train, label=f'Train deg={deg}', color=color)

        y_pred_test = evaluate_polynomial(coeffs, x_test)
        plt.plot(x_test, y_pred_test, '--', label=f'Test deg={deg}', color=color)

        metrics = evaluate_accuracy(y_test, y_pred_test)
        print(f"Degree {deg} → MAPE (%): {metrics['MAPE (%)']:.4f}")

    u = np.zeros_like(dy)
    plt.quiver(x, y, u, dy, angles='xy', scale_units='xy', scale=1, color='gray', label='Estimated Derivative')
    plt.legend()
    plt.xlabel("Time Index")
    plt.ylabel("Stock Price")
    plt.title("Stock Price Forecast with Interpolation and Regression")
    plt.grid(True)
    plt.show()