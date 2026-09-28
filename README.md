# MEXCode

MEXCode (Mathematical Expressions × Code) is a Python library for representing mathematical expressions and using tools to perform operations on them.

## Disclaimer

This project is in early development. The Python source is functional, but the C++ source is not yet present. The Python source is not yet packaged for installation, and the repository does not yet include build configuration.

This project is intended to utilize C++ lower level implementations for performance, while using Python for higher level operations and user interface.

## Features

- Represent monomial terms and polynomials.
- Evaluate expressions and compute tables of values.
- Differentiate and integrate supported polynomial expressions symbolically.
- Use numerical helpers for callable expressions, including differentiation, integration, average value, and zero finding.

## Quick Start

The Python source is under `python/src`. From the repository root, set it on `PYTHONPATH` and create a `Function`:

```powershell
$env:PYTHONPATH = "$PWD/python/src"
python -c "from calculus.functions import Function, MonomialTerm; curve = Function([MonomialTerm(coefficient=2, exponent=1)]); print(curve.integrate(0, 3))"
```

This defines $f(x)=2x$ and calculates its exact definite integral from 0 to 3, which is `9`.

Callable expressions can use the numerical helpers:

```python
from calculus.general import derivative, integrate

curve = lambda x: 2 * x
print(derivative(curve)(3))
print(integrate(curve, 0, 3))
```

The helpers in `calculus.general` are numerical approximations. For polynomial expressions, use `Function.integrate` for symbolic integration.

## Project Layout

```text
python/
	src/
		calculus/
			functions.py  # Expression classes and symbolic calculus operations
			general.py    # Numerical helpers for callable expressions
cpp/
```

The Python package is currently run directly from `python/src`; the repository does not yet include installation or build configuration.

## License

MEXCode is released under the MIT License. See [LICENSE](LICENSE).
