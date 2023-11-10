AtomicBasisFunction Class Documentation
Overview
The AtomicBasisFunction class is designed to represent atomic basis functions, which are essential in quantum chemistry for the computation of molecular orbitals. This class allows for the calculation of Gaussian function values for different atomic orbitals.

Class Methods
__init__(self, numbers, alphas, linear)
Initializes the AtomicBasisFunction class with orbital numbers, alpha values, and linear coefficients.

Parameters
numbers: A list of the number of orbitals.
alphas: A list of alpha values for the Gaussian functions.
linear: A list of linear coefficients for the linear combination of Gaussian functions.
Returns
This method does not return any value.

Gaussian Function Methods
These methods calculate Gaussian functions for various atomic orbitals:

gaussian_1s(alpha, x, y, z): Calculates the 1s Gaussian function.
gaussian_2s(alpha, x, y, z): Calculates the 2s Gaussian function.
gaussian_2px(alpha, x, y, z): Calculates the 2px Gaussian function.
gaussian_2py(alpha, x, y, z): Calculates the 2py Gaussian function.
gaussian_2pz(alpha, x, y, z): Calculates the 2pz Gaussian function.
Each of these methods takes alpha (a Gaussian function parameter) and (x, y, z) coordinates as inputs.

evaluate(self, x, y, z)
Evaluates the atomic basis function at given (x, y, z) coordinates by summing up the contributions of all Gaussians.

Parameters
x, y, z: The coordinates at which to evaluate the function.
Returns
The evaluated atomic basis function value.
vector_function(self, positions)
Evaluates the atomic basis function at multiple (x, y, z) coordinates and returns a vector of the results.

Parameters
positions: A list of (x, y, z) coordinates.
Returns
A numpy array containing the evaluated values and their corresponding positions.
Usage Example
python
Copy code
# Example of using AtomicBasisFunction class
atomic_basis = AtomicBasisFunction(numbers, alphas, linear)
value = atomic_basis.evaluate(x, y, z)
vector_values = atomic_basis.vector_function(positions)
WannierBasisFunction Class Documentation
Overview
The WannierBasisFunction class represents Wannier basis functions for molecular systems, providing methods to calculate Wannier functions and molecular vector functions.

Class Methods
__init__(self)
Initializes a new instance of the WannierBasisFunction class.

Parameters
This method does not take any parameters.

Returns
This method does not return any value.

calculateWannier(self, func_1, func_2, beta, gamma)
Calculates the Wannier function from two input functions and scaling parameters.

Parameters
func_1: The first atomic basis function.
func_2: The second atomic basis function.
beta: A scaling parameter.
gamma: Another scaling parameter.
Returns
The calculated Wannier function value.
vector_molecular_function(self, functions, coeffs)
Computes a molecular vector function from a set of input functions and coefficients.

Parameters
functions: A list of atomic basis functions.
coeffs: A list of coefficients for the functions.
Returns
The computed molecular vector function.
Usage Example
python
Copy code
# Example of using WannierBasisFunction class
wannier_function = WannierBasisFunction()
result = wannier_function.calculateWannier(func1, func2, beta, gamma)
molecular_vector = wannier_function.vector_molecular_function([func1, func2], [coeff1, coeff2])
