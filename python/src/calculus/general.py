"""

    ### mexcode.calculus.general

    This module contains general calculus functions and utilities such
    as differentiation and integration. It provides standalone Python
    functions that can be used to perform calculus operations on mathematical
    expressions that are represented as lambda functions or other callable objects. 
    This is best used for when working with small expressions. 
    
    For larger ones, it is recommended to use the `Function` class from the `functions`
    module, which provides a more structured and efficient way to represent and manipulate 
    large mathematical functions and expressions.
    
    Example usage:
    
    ```python
    from mexcode.calculus.general import differentiate

    quadratic = lambda x: 3 * x**2 + 2*x + 1
    derivative = differentiate(quadratic)
    print(derivative(5))  # Output: 32
    ```

"""

from collections.abc import Callable


def derivative(expression: Callable[[float], float]) -> Callable[[float], float]:
    """
    Computes the derivative of a given mathematical expression represented as a callable object (e.g., a lambda function).

    Args:
        expression (Callable[[float], float]): A callable function representing the mathematical expression to differentiate.
    """
    def derivative_function(x: float, h: float = 1e-3) -> float:
        return (expression(x + h) - expression(x - h)) / (2 * h)

    return derivative_function

def dydx(expression: Callable[[float], float]) -> Callable[[float], float]:
    """Short alias for the `derivative` function."""
    return derivative(expression)

def integrate(expression: Callable[[float], float], lower_bound: float, upper_bound: float, num_intervals: int = 1000) -> float:
    """
    Computes the definite integral of a given mathematical expression represented as a callable object (e.g., a lambda function) over a specified interval.
    Note that this function uses numerical integration (the trapezoidal rule) to approximate the integral, and therefore will not yield as accurate results
    as the `integrate` method of the `Function` class in the `functions` module, which uses symbolic integration.

    Args:
        expression (Callable[[float], float]): A callable function representing the mathematical expression to integrate.
        lower_bound (float): The lower bound of the integration interval.
        upper_bound (float): The upper bound of the integration interval.
        num_intervals (int, optional): The number of intervals to use for numerical integration. Default is 1000.

    Returns:
        float: The approximate value of the definite integral over the specified interval.
    """
    width = (upper_bound - lower_bound) / num_intervals
    total_area = 0.0

    for i in range(num_intervals):
        x = lower_bound + i * width
        total_area += expression(x) * width

    return total_area

def avg_val(expression: Callable[[float], float], lower_bound: float, upper_bound: float, num_intervals: int = 1000) -> float:
    """
    Computes the average value of a given mathematical expression represented as a callable object (e.g., a lambda function) over a specified interval.
    Note that this function uses numerical integration (the trapezoidal rule) to approximate the integral, and therefore will not yield as accurate results
    as the `avg_val` method of the `Function` class in the `functions` module, which uses symbolic integration.

    Args:
        expression (Callable[[float], float]): A callable function representing the mathematical expression to compute the average value for.
        lower_bound (float): The lower bound of the integration interval.
        upper_bound (float): The upper bound of the integration interval.
        num_intervals (int, optional): The number of intervals to use for numerical integration. Default is 1000.

    Returns:
        float: The approximate average value of the expression over the specified interval.
    """

    integral_value: float = integrate(expression, lower_bound, upper_bound, num_intervals)
    average_value: float = integral_value / (upper_bound - lower_bound)
    return average_value

def zeroes(expression: Callable[[float], float], lower_bound: float, upper_bound: float, num_points: int = 1000) -> list[float]:
    """
    Finds the zeroes (roots) of a given mathematical expression represented as a callable object (e.g., a lambda function) within a specified interval.
    Note that this function uses numerical methods to approximate the roots, and therefore may not yield as accurate results
    as the `zeroes` method of the `Function` class in the `functions` module, which uses symbolic methods.

    Args:
        expression (Callable[[float], float]): A callable function representing the mathematical expression to find roots for.
        lower_bound (float): The lower bound of the interval to search for roots.
        upper_bound (float): The upper bound of the interval to search for roots.
        num_points (int, optional): The number of points to sample within the interval. Default is 1000.

    Returns:
        list[float]: A list of approximate roots found within the specified interval.
    """
    step = (upper_bound - lower_bound) / num_points
    roots: list[float] = []

    for i in range(num_points):
        x1 = lower_bound + i * step
        x2 = x1 + step
        if expression(x1) * expression(x2) < 0:  # Check for sign change
            root = (x1 + x2) / 2  # Approximate root as midpoint
            roots.append(root)

    return roots

