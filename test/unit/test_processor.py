import sys
import unittest
import random
import numpy as np
import pandas as pd
import filecmp
import os
sys.path.append('../../')
import data_processor as dtp  # nopep8


class TestData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rand_seed = random.randint(1, 100)
        # ensure different matrices for negative test with wrong_seed
        cls.wrong_seed = random.randint(cls.rand_seed + 1, cls.rand_seed + 50)
        cls.N = random.randint(1, 10)
        cls.M = random.randint(1, 10)
        np.random.seed(cls.rand_seed)
        cls.random_matrix = np.random.rand(cls.N, cls.M)
        np.random.seed(cls.wrong_seed)
        cls.wrong_matrix = np.random.rand(cls.N, cls.M)
        os.mkdir("test_files")
        pd.DataFrame(cls.random_matrix).to_csv(
            "test_files/random.csv", header=None)
        pd.DataFrame(cls.wrong_matrix).to_csv(
            "test_files/wrong.csv", header=None)

    @classmethod
    def tearDownClass(cls):
        print("Running tearDownClass")
        dir = "./test_files/"
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        os.rmdir("test_files")

    def test_get_random_matrix(self):
        test_matrix = dtp.get_random_matrix(self.N, self.M, self.rand_seed)

        # positive test : test that the correct matrix is returned
        self.assertTrue(np.all(np.equal(test_matrix, self.random_matrix)))

        # negative test : test that the returned matrix doesn't
        # equal another matrix
        self.assertTrue(np.any(np.not_equal(test_matrix, self.wrong_matrix)))

        # exception test : test that an exception is raised if
        # N and M are not integers or less than zero
        self.assertRaises(Exception, dtp.get_random_matrix, 1.231, 7.890)
        self.assertRaises(Exception, dtp.get_random_matrix, -12, -1)

    def test_get_file_dimesions(self):
        csv_name = "../../iris.data"
        dimensions = dtp.get_file_dimensions(csv_name)

        # positive test : test that the correct dimensions are returned
        self.assertEqual(dimensions, (150, 5))

        # negative test : test that function output
        # doesn't equal the wrong dimensions
        self.assertNotEqual(dimensions, 10, 15)

    def test_write_matrix_to_file(self):
        dtp.write_matrix_to_file(
            self.N, self.M, "test_files/test.csv", self.rand_seed)

        # positive test : test that the correct file is written
        self.assertTrue(
            filecmp.cmp("test_files/test.csv", "test_files/random.csv"))

        # negative test : test that an incorrect file doesn't equal
        # the written file
        self.assertFalse(
            filecmp.cmp("test_files/test.csv", "test_files/wrong.csv"))


if __name__ == '__main__':
    unittest.main()
