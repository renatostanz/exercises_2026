import numpy as np
import numpy.typing as npt

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    # Your code here
    f_derivative_coeffs = [coeff * i for i, coeff in enumerate(f_coeffs) if i > 0]
    g_derivative_coeffs = [coeff * i for i, coeff in enumerate(g_coeffs) if i > 0]

    f_degree = len(f_coeffs) - 1
    g_degree = len(g_coeffs) - 1
    def polinomial_coeffs_product(a: list, b: list) -> npt.NDArray[np.float64]:
        r = np.zeros(f_degree + g_degree)
        for i, a_coeff in enumerate(a):
            for j, b_coeff in enumerate(b):
                offset = i + j
                r[offset] += a_coeff * b_coeff
        
        return r if r.size > 0 else np.zeros(1)

    # (f * g)' = f * g' + f' * g
    return (
        polinomial_coeffs_product(f_coeffs, g_derivative_coeffs) + \
        polinomial_coeffs_product(f_derivative_coeffs, g_coeffs)
    ).tolist()
