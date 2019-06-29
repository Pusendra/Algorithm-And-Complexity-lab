class Binary_Search_Tree:
	def __init__(self):
		self._size = 0
		self._root = None

	class Node:
		def __init__(self, key, value):
			self.key = key
			self.value = value
			self.left = None
			self.right = None

	#for inserting nodes in binary search tree
	def insertNode(self, key, value):
		u = self._BSTNode(key, value)
		w =None
		v = self._root
		while (v != None):
			w = v
			if (key < v.key):
				v = v.left
			else:
				v = v.right
		if (w == None):
			self._root = u
		elif (u.key < w.key):
			w.left = u
		else:
			w.right = u
		self._size += 1

	def isEmpty(self):
		return self._size == 0

	def size(self):
		return self._size
	#for inorder traversal
	def inOrder(self):
		nodes = []
		self._inOrder(self._root, nodes)
		return nodes

	def _inOrder(self, subtree, nodes):
		if(subtree):
			self._inOrder(subtree.left, nodes)
			nodes.append(subtree.key)
			self._inOrder(subtree.right, nodes)
   #for preorder traversal
	def preOrder(self):
		nodes = []
		self._preOrder(self._root, nodes)
		return nodes

	def _preOrder(self, subtree, nodes):
		if(subtree):
			nodes.append(subtree.key)
			self._preOrder(subtree.left, nodes)
			self._preOrder(subtree.right, nodes)
	#for postorder traversal
	def postOrder(self):
		nodes = []
		self._postOrder(self._root, nodes)
		return nodes

	def _postOrder(self, subtree, nodes):
		if(subtree):
			self._preOrderTraverse(subtree.left, nodes)
			self._preOrderTraverse(subtree.right, nodes)
			nodes.append(subtree.key)
	#searching nodes in binary search tree
	def searchNode(self, key):
		found = []
		self._searchNode(self._root, key, found)
		return found

	def _searchNode(self, subtree, key, found):
		if(subtree):
			if(key == subtree.key):
				found.append(1)
			elif(key < subtree.key):
				self._searchForNode(subtree.left, key, found)
			elif(key > subtree.key):
				self._searchForNode(subtree.right, key, found)
	#for finding smallest number in binary search tree
	def Smallest_Key(self):
		nodes = []
		self._Smallest_Key(self._root, nodes)
		return nodes

	def _Smallest_Key(self, subtree, nodes):
		if(subtree):
			if(subtree.left == None):
				nodes.append(subtree.key)
			self._SmallestKey(subtree.left, nodes)
	#for finding largest number in binary serach tree
	def Largest_Key(self):
		nodes = []
		self._Largest_Key(self._root, nodes)
		return nodes

	def _Largest_Key(self, subtree, nodes):
		if(subtree):
			if(subtree.right == None):
				nodes.append(subtree.key)
			self._findLargest_Key(subtree.right, nodes)
	#for deleting nodes
#	def deletenode(self, key):
#		if self.root is not None:
#			if self.root.key == key:
#				self.root = None
#				self.size -= 1
#				return True
#			if self.find(key) is None:
#				return False
#			if self.root.deletenode(key):
#				self.size -= 1
