import unittest
from binary_search import binary_search

class SearchTestCase(unittest.TestCase):

	def test_binary_search(self):
		values=[5,2,4,9,0,6,1]

		#To check whether assertion is true or false
		self.assertEqual(binary_search(values,9),9)
		self.assertEqual(binary_search(values,1),1)
		self.assertEqual(binary_search(values,7),-1)


if __name__=="__main__":
	unittest.main()
