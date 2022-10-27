import sys
import unittest
import random
import numpy as np
import pandas as pd
sys.path.append('../../')
import data_processor as dtp  # nopep8


class TestProcessor(unittest.TestCase):

    def test_get_random_matrix(self):
        rand_seed = random.randint(1, 100)
        # ensure different matrices for negative test with wrong_seed
        wrong_seed = random.randint(rand_seed + 1, rand_seed + 50)
        N = random.randint(1, 10)
        M = random.randint(1, 10)
        test_matrix = dtp.get_random_matrix(N, M, rand_seed)

        np.random.seed(rand_seed)
        random_matrix = np.random.rand(N, M)
        np.random.seed(wrong_seed)
        wrong_matrix = np.random.rand(N, M)

        # positive test : test that the correct matrix is returned
        self.assertTrue(np.all(np.equal(test_matrix, random_matrix)))

        # negative test : test that the returned matrix doesn't
        # equal another matrix
        self.assertTrue(np.any(np.not_equal(test_matrix, wrong_matrix)))

        # exception test : test that an exception is raised if
        # N and M are not integers or less than zero
        self.assertRaises(Exception, dtp.get_random_matrix, 1.231, 7.890)
        self.assertRaises(Exception, dtp.get_random_matrix, -12, -1)

    def test_get_file_dimesions(self):
        csv_name = "iris.data"
        dimensions = get_file_dimensions(csv_name)

        # positive test : test that the correct dimensions are returned
        self.assertEqual(dimensions, (150, 5))

        # negative test : test that function output
        # doesn't equal the wrong dimensions
        self.assertNotEqual(dimensions, 10, 15)

if __name__ == '__main__':
    unittest.main()
