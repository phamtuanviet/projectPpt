import numpy as np
import matplotlib.pyplot as plt

def mean_absolute_percentage_error(y_true, y_pred):
    """MAPE – Mean Absolute Percentage Error (%)"""
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    nonzero = y_true != 0  # Tránh chia cho 0
    return np.mean(np.abs((y_true[nonzero] - y_pred[nonzero]) / y_true[nonzero])) * 100


def evaluate_accuracy(y_true, y_pred):
    return {
        'MAPE (%)': mean_absolute_percentage_error(y_true, y_pred)
    }
