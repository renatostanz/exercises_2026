def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'column':
        cols_sums = matrix[0]
        for row in matrix[1:]:
            for i, val in enumerate(row):
                cols_sums[i] += val

        return [col_sum / len(matrix) for col_sum in cols_sums]

    return [float(sum(row)) / len(matrix[0]) for row in matrix]
