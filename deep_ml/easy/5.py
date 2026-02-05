def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	return [
        [value * scalar for value in row] for row in matrix
    ] 
