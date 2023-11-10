# `basis.py` Module Documentation

## Overview

The `basis.py` module in the `src` directory contains two key classes: `AtomicBasisFunction` and `WannierBasisFunction`. These classes are designed for computations in quantum chemistry, specifically for the handling of atomic and molecular orbitals using Gaussian basis functions and Wannier functions.

## Classes

### AtomicBasisFunction

#### Description

The `AtomicBasisFunction` class provides methods to compute Gaussian function values for different atomic orbitals.

#### Initialization

```python
def __init__(self, numbers, alphas, linear):

Initializes the class with the number of orbitals (numbers), alpha values for the Gaussian functions (alphas), and linear coefficients for the linear combination (linear).

Methods
gaussian_1s(alpha, x, y, z): Computes the 1s Gaussian function.
gaussian_2s(alpha, x, y, z): Computes the 2s Gaussian function.
gaussian_2px(alpha, x, y, z): Computes the 2px Gaussian function.
gaussian_2py(alpha, x, y, z): Computes the 2py Gaussian function.
gaussian_2pz(alpha, x, y, z): Computes the 2pz Gaussian function.
evaluate(x, y, z): Evaluates the atomic basis function at given coordinates.
vector_function(positions): Evaluates the function at multiple coordinates.
