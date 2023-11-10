import unittest
import numpy as np
from basis import AtomicBasisFunction, WannierBasisFunction

class TestAtomicBasisFunction(unittest.TestCase):

    def setUp(self):
        # Example initialization
        self.numbers = [2, 0, 1, 0, 1]  # Just an example
        self.alphas = [[1, 2], [], [3], [], [4]]
        self.linear = [[5, 6], [], [7], [], [8]]
        self.atomic_basis = AtomicBasisFunction(self.numbers, self.alphas, self.linear)

    def test_gaussian_1s(self):
        # Test the gaussian_1s function
        result = self.atomic_basis.gaussian_1s(1, 0, 0, 0)
        self.assertAlmostEqual(result, (1 / np.pi) ** (3 / 2))

    # Add tests for other Gaussian functions...

    def test_evaluate(self):
        # Test the evaluate function
        # This test will depend on your specific implementation and may need to be adjusted
        result = self.atomic_basis.evaluate(0, 0, 0)
        self.assertTrue(isinstance(result, float))

    def test_vector_function(self):
        # Test the vector_function method
        positions = [[0, 0, 0], [1, 1, 1]]
        result = self.atomic_basis.vector_function(positions)
        self.assertEqual(result.shape, (2, 4))

class TestWannierBasisFunction(unittest.TestCase):

    def setUp(self):
        self.wannier_basis = WannierBasisFunction()

    def test_calculateWannier(self):
        # Test the calculateWannier function
        result = self.wannier_basis.calculateWannier(1, 2, 3, 4)
        self.assertEqual(result, 3 * (1 - 4 * 2))

    def test_vector_molecular_function(self):
        # Test the vector_molecular_function
        functions = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        coeffs = [7, 8]
        result = self.wannier_basis.vector_molecular_function(functions, coeffs)
        self.assertTrue(np.array_equal(result, 7 * (functions[0] - 8 * functions[1])))

if __name__ == '__main__':
    unittest.main()
