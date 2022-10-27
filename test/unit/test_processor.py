import sys
import unittest
import random
import numpy as np
sys.path.append('../../')
import data_processor as dtp #nopep8

class TestProcessor(unittest.TestCase):

#	@classmethod
#	def setUpClass(cls):

#	@classmethod
#	def tearDownClass(cls):

	def test_get_random_matrix(self):
		np.random.seed(17)
		N = random.randint(1, 10)
		# ensure N and M are different for negative test
		M = random.randint(N + 1, N + 11)

		random_matrix = np.random.rand(N, M)
		wrong_matrix = np.random.rand(M, N)

		# positive test : test that the correct matrix is returned
		self.assertEqual(random_matrix.all(), dtp.get_random_matrix(N, M).all())

		# negative test : test that the returned matrix doesn't
		# equal another matrix
		self.assertNotEqual(wrong_matrix.all(), dtp.get_random_matrix(M, N).all())

		# exception test : test that an exception is raised if
		# N and M are not integers or less than zero
		self.assertRaises(Exception, dtp.get_random_matrix, 1.231, 7.890)
		self.assertRaises(Exception, dtp.get_random_matrix, -12, -1)

if __name__ == '__main__':
	unittest.main()
