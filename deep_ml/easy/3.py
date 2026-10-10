def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    total_values_in_a = len(a) * len(a[0])
    if total_values_in_a != new_shape[0] * new_shape[1]:
        return []

    aux_count = 0
    reshaped_matrix = [[]]
    for line in a:
        for val in line:
            aux_count += 1
            reshaped_matrix[-1].append(val)
            if len(reshaped_matrix[-1]) >= new_shape[1] and len(reshaped_matrix) < new_shape[0]:
                reshaped_matrix.append([])
                aux_count = 0

    return reshaped_matrix
