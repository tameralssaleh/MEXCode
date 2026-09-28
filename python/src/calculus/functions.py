"""

    ### mexcode.calculus.functions

    This module is part of the calculus package of MEXcode and contains classes and methods
    for performing calculus operations on mathematical functions. It provides a `FunctionBuilder` 
    class that can be used to build dedicated functions and perform calculus operations on them, 
    such as differentiation and integration.

"""


from typing import Any

class MonomialTerm:
    """
    Takes in a coefficient, and an exponent.

    `coefficient:` float | default: 1\n
    `exponent:` int | default: 1
    """
    def __init__(self, coefficient: float = 1, exponent: int = 1):
        self.coefficient = coefficient
        self.exponent = exponent

    def __str__(self) -> str:
        """Returns a string representation of the monomial term.

        Returns:
            str: _description_
        """
        if self.exponent == 0:
            return f"{self.coefficient}"
        elif self.exponent == 1:
            return f"{self.coefficient}x"
        else:
            return f"{self.coefficient}x^{self.exponent}"

    def __repr__(self) -> str:
        """Returns a string representation of the monomial term.

        Returns:
            str: _description_
        """
        return self.__str__()

    def __add__(self, other: "MonomialTerm") -> "MonomialTerm":
        """Adds two monomial terms together. If the exponents are not the same, it will raise a ValueError.

        Args:
            other (MonomialTerm): _description_

        Returns:
            MonomialTerm: _description_
        """
        if self.exponent != other.exponent:
            raise ValueError("Exponents must be the same to add monomial terms.")
        return MonomialTerm(coefficient=self.coefficient + other.coefficient, exponent=self.exponent)

    def __mul__(self, other: "MonomialTerm") -> "MonomialTerm":
        """Multiplies two monomial terms together.

        Args:
            other (MonomialTerm): _description_

        Returns:
            MonomialTerm: _description_
        """
        return MonomialTerm(coefficient=self.coefficient * other.coefficient, exponent=self.exponent + other.exponent)

    def __truediv__(self, other: "MonomialTerm") -> "MonomialTerm":
        """Divides two monomial terms together.

        Args:
            other (MonomialTerm): _description_

        Returns:
            MonomialTerm: _description_
        """
        return MonomialTerm(coefficient=self.coefficient / other.coefficient, exponent=self.exponent - other.exponent)

    def __pow__(self, power: int) -> "MonomialTerm":
        """Raises a monomial term to a power.

        Args:
            power (int): _description_

        Returns:
            MonomialTerm: _description_
        """
        return MonomialTerm(coefficient=self.coefficient ** power, exponent=self.exponent * power)

    def evaluate(self, x: float) -> float:
        """Evaluates the monomial term at a given point `x`.

        Args:
            x (float): input value to evaluate the monomial term at.

        Returns:
            float: output value of the monomial term at the given point `x`.
        """
        return self.coefficient * (x ** self.exponent)

class Polynomial:
    """
    Takes in a list of monomial terms and joins them to create a polynomial.
    Automatically combines like terms.

    `terms:` list[`MonomialTerm`]\n
    `c (constant):` float | default: 0 
    
    """
    def __init__(self, terms: list[MonomialTerm], c: float = 0):
        self.terms = terms
        self.c = c

    def evaluate(self, x: float) -> float:
        """Evaluates the polynomial at a given point `x`.

        Args:
            x (float): input value to evaluate the polynomial at.

        Returns:
            float: output value of the polynomial at the given point `x`.
        """
        result = self.c
        for term in self.terms:
            result += term.evaluate(x)
        return result

class Function:
    """Turns any type of expression into a workable function."""
    def __init__(self, workable_expression: Any):
        self.workable_expression = workable_expression

    def compute(self, x: float) -> float:
        """Returns the value of the function at a given point `x`. In other words, return the value of `y` given `x`.

        Args:
            x (float): input value to evaluate the function at.

        Returns:
            float: output value of the function at the given point `x`.
        """

        result = 0

        for expression in self.workable_expression:
            if isinstance(expression, MonomialTerm):
                result += expression.evaluate(x)
            elif isinstance(expression, Polynomial):
                result += expression.evaluate(x)
            else:
                raise TypeError(f"Unsupported expression type: {type(expression)}")
            
        return result

    def compute_table(self, x_values: list[float]) -> list[float]:
        """Returns a list of values of the function at given points `x_values`. In other words, return the value of `y` given `x`.

        Args:
            x_values (list[float]): input values to evaluate the function at.

        Returns:
            list[float]: a list of output values of the function at the given points.
        """
        return [self.compute(x) for x in x_values]

    def differentiate(self) -> "Function":
        """Returns the derivative of the function.

        Returns:
            Function: the derivative of the function.
        """
        differentiated_terms: list[MonomialTerm] = []
        for expression in self.workable_expression:
            if isinstance(expression, MonomialTerm):
                differentiated_terms.append(MonomialTerm(coefficient=expression.coefficient * expression.exponent, exponent=expression.exponent - 1))
            elif isinstance(expression, Polynomial):
                differentiated_terms.extend([MonomialTerm(coefficient=term.coefficient * term.exponent, exponent=term.exponent - 1) for term in expression.terms])
            else:
                raise TypeError(f"Unsupported expression type: {type(expression)}")
        
        return Function(differentiated_terms)

    def indefinite_integral(self) -> "Function":
        """Returns the indefinite integral of a function. Note that this logic does not include the constant of integration at the end, so it should be manually interpreted as if it does when needed.

        Returns:
            Function: The indefinite integral of the function.
        """
        integrated_terms: list[MonomialTerm] = []
        for expression in self.workable_expression:
            if isinstance(expression, MonomialTerm):
                integrated_terms.append(MonomialTerm(coefficient=expression.coefficient / (expression.exponent + 1), exponent=expression.exponent + 1))
            elif isinstance(expression, Polynomial):
                integrated_terms.extend([MonomialTerm(coefficient=term.coefficient / (term.exponent + 1), exponent=term.exponent + 1) for term in expression.terms])
            else:
                raise TypeError(f"Unsupported expression type: {type(expression)}")
        
        return Function(integrated_terms)

    def integrate(self, a: float, b: float) -> float:
        """Returns the definite integral of a function between two points `a` and `b`.

        Args:
            a (float): lower limit of integration.
            b (float): upper limit of integration.

        Returns:
            float: the definite integral of the function between `a` and `b`.
        """

        antiderivative = self.indefinite_integral()
        return antiderivative.compute(b) - antiderivative.compute(a)
