
import unittest
from MergeSort import merge_sort

class TestSearch(unittest.TestCase):
    
    def test_merge_sort(self):

        
        list_1 = [1, 9 ,6 , 7 ,8]
        merge_sort(list_1, 0, len(list_1))
        self.assertListEqual(list_1, [1, 6, 7, 8, 9])

        list_2 = [1, 2, 8, 4 , 9 , 5]
        merge_sort(list_2, 0, len(list_2))
        self.assertListEqual(list_2, [1, 2, 4, 5, 8,9])

        list_3 = [5,9,8,6,4,1]
        merge_sort(list_3, 0, len(list_3))
        self.assertListEqual(list_3, [1, 4, 5, 6 , 8, 9])

       
        

if __name__ == "__main__":
    unittest.main()
