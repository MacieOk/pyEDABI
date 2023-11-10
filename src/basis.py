import numpy as np

class AtomicBasisFunction:
    """
    Represents an atomic basis function. Allows for the computation of Gaussian
    function values for different atomic orbitals.
    """

    def __init__(self, numbers, alphas, linear):
        """
        Initializes the class with lists of the number of orbitals, alpha values for the
        Gaussian functions, and linear coefficients for the linear combination.
        """
        self.numbers = numbers
        self.alphas = alphas
        self.linear = linear

    def gaussian_1s(self, alpha, x, y, z):
        """
        Calculates the 1s Gaussian function for a given alpha and (x, y, z) coordinates.
        """
        return (alpha / np.pi) ** (3 / 2) * np.exp(-alpha * (x ** 2 + y ** 2 + z ** 2))

    def gaussian_2s(self, alpha, x, y, z):
        """
        Calculates the 2s Gaussian function for a given alpha and (x, y, z) coordinates.
        """
        r2 = x ** 2 + y ** 2 + z ** 2
        return (alpha / np.pi) ** (3 / 2) * (2 * alpha * r2 - 1) * np.exp(-alpha * r2)

    def gaussian_2px(self, alpha, x, y, z):
        """
        Calculates the 2px Gaussian function for a given alpha and (x, y, z) coordinates.
        """
        return (alpha / np.pi) ** (3 / 2) * x * np.exp(-alpha * (x ** 2 + y ** 2 + z ** 2))

    def gaussian_2py(self, alpha, x, y, z):
        """
        Calculates the 2py Gaussian function for a given alpha and (x, y, z) coordinates.
        """
        return (alpha / np.pi) ** (3 / 2) * y * np.exp(-alpha * (x ** 2 + y ** 2 + z ** 2))

    def gaussian_2pz(self, alpha, x, y, z):
        """
        Calculates the 2pz Gaussian function for a given alpha and (x, y, z) coordinates.
        """
        return (alpha / np.pi) ** (3 / 2) * z * np.exp(-alpha * (x ** 2 + y ** 2 + z ** 2))

    def evaluate(self, x, y, z):
        """
        Evaluates the atomic basis function at given (x, y, z) coordinates by summing
        up the contributions of all Gaussians.
        """
        total = 0
        for n, num_orbitals in enumerate(self.numbers):
            if num_orbitals != 0:
                for i in range(num_orbitals):
                    if i < len(self.alphas[n]) and i < len(self.linear[n]):
                        total += self.linear[n][i] * self.gaussian_1s(self.alphas[n][i], x, y, z)
        return total

    def vector_function(self, positions):
        """
        Evaluates the atomic basis function at multiple (x, y, z) coordinates and
        returns a vector of the results.
        """
        result = []
        for pos in positions:
            value = self.evaluate(pos[0], pos[1], pos[2])
            result.append([value, *pos])

        return np.array(result)


class WannierBasisFunction:
    """
    Represents a Wannier basis function for molecular systems. Provides methods
    to calculate Wannier functions and molecular vector functions.
    """

    def __init__(self):
        pass

    def calculateWannier(self, func_1, func_2, beta, gamma):
        """
        Calculates the Wannier function from two input functions and scaling
        parameters beta and gamma.
        """
        val_wannier = beta * (func_1 - gamma * func_2)
        return val_wannier

    def vector_molecular_function(self, functions, coeffs):
        """
        Computes a molecular vector function from a set of input functions and
        coefficients.
        """
        return coeffs[0] * (functions[0] - coeffs[1] * functions[1])




