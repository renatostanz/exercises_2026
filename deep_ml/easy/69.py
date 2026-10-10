import numpy as np

def r_squared(y_true, y_pred):
    residual_sum = np.sum(np.square((y_true - y_pred)))
    total_sum = np.sum(np.square((y_pred - np.mean(y_pred))))

    if total_sum == 0:
        return 0

    return 1 - (residual_sum / total_sum)


