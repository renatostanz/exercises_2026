import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.

    Args:
        gradient: A list representing the gradient vector

    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    # Your code here
    magnitude = sum(i*i for i in gradient) ** (1/2)
    unit_vector = [
        i / magnitude if i != 0 else 0
        for i in gradient
    ]
    return {
        "magnitude": magnitude,
        "direction": unit_vector,
        "descent_direction": [-i for i in unit_vector]
    }
