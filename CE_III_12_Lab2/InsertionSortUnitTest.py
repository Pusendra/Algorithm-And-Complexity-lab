
import unittest
from InsertionSort import insertion_sort

class TestSearch(unittest.TestCase):
    
    def test_insertion_sort(self):
        
        self.assertListEqual(insertion_sort([1,6,8,2,3]), [1,2,3,6,8])
        self.assertListEqual(insertion_sort([8,5,1,4,3]), [1,4,3,5,8])
        self.assertListEqual(insertion_sort([1,6,30,2,3]), [1,2,3,6,30])
        self.assertListEqual(insertion_sort([5,8,9,4,6]), [4,5,6,8,9])

if __name__ == "__main__":
    unittest.main()
