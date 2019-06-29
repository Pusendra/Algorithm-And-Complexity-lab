import unittest
from BinarySearchTree import Binary_Search_Tree

class BSTTestCase(unittest.TestCase):
	def testBinarySearch(self):
		bst = BinarySearchTree()

		bst.insertNode(30, "Value 1")
		self.assertEqual(bst.size(),1)

		bst.insertNode(25, "Value 2")
		self.assertEqual(bst.size(),2)

		bst.insertNode(5, "Value 2")
		self.assertEqual(bst.size(),3)

		self.assertListEqual(bst.inOrder(), [30, 40, 15])
		self.assertListEqual(bst.preOrder(), [10, 25, 12])
		self.assertListEqual(bst.postOrder(), [12, 38, 22])

		self.assertListEqual(bst.searchSmallestKey(), 5)
		self.assertListEqual(bst.searchLargestKey(), [30])

		self.assertEqual(bst.searchForNode(30), [1])
		# deleting nodes:
		# (bst.deletenode(30)
		# bst.deletenode(2)
        # del l[1]
        # self.assertListEqual(bt.inorder(), sorted(l)))

if __name__  == '__main__':
	unittest.main()
