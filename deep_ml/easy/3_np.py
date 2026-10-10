import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
        return []

    arr = np.array(a)
    return arr.reshape(new_shape).tolist()
