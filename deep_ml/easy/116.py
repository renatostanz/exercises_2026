def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    if n == 0:
        return 0.0

    new_n = n-1
    return c * (x**new_n) * n
