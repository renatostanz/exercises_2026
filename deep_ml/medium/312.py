import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g_degree = len(g_coeffs) - 1
    g_coeffs_derivate = [coeff * (g_degree - i) for i, coeff in enumerate(g_coeffs) if i < g_degree]

    h_degree = len(h_coeffs) - 1
    h_coeffs_derivate = [coeff * (h_degree - i) for i, coeff in enumerate(h_coeffs) if i < h_degree]

    def coeffs_polynomial_product(a: list, b:list) -> list:
        result = np.zeros(len(a) + len(b) - 1)

        for i, value_a in enumerate(a):
            for j, value_b in enumerate(b):
                result[i+j] += value_a * value_b

        return result if result.size > 0 else [0.0]


    numerator = (
        coeffs_polynomial_product(g_coeffs_derivate, h_coeffs) -
        coeffs_polynomial_product(h_coeffs_derivate, g_coeffs)
    )

    denominator = coeffs_polynomial_product(h_coeffs, h_coeffs)


    def get_value_in_x(polynomial_coeffs: list) -> float:
        result = 0.0
        for n, coeff in enumerate(reversed(polynomial_coeffs)):
            result += coeff * (x ** n)

        return result


    return get_value_in_x(numerator) / get_value_in_x(denominator)
