import unittest
from linear_search import linear_search

class SearchTestCase(unittest.TestCase):

	def test_linear_search(self):
		values=[5,2,4,9,0,6,1]
		self.assertEqual(linear_search(values,9),9)
		self.assertEqual(linear_search(values,1),1)
		self.assertEqual(linear_search(values,7),-1)

if __name__=="__main__":
	unittest.main()
