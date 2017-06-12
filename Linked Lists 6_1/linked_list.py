class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	# returns number of data elements in list
	def num_elems(self):
		return self.size

	# bool returns true if empty
	def is_empty(self):
		if self.size == 0:
			return True
		return False

	# returns the value of the nth item (starting at 0 for first)
	def value_at(self, index):
		i = 0
		ptr = self.head
		while (i < index):
			ptr = ptr.next
			i += 1
		return ptr

	# adds an item to the front of the list
	def push_front(self, value):
		# make a new node, then point it to current head, then set the new node to the head
		new_head = Node(value)
		new_head.next = self.head
		self.size += 1
		self.head = new_head

	# remove front item and return its value
	def pop_front(self):
		new_head = self.head.next
		val = self.head.data
		self.head = self.head.next
		self.size -= 1
		return val

	# adds an item at the end
	def push_back(self, value):
		ptr = self.head
		while ptr.next != None:
			ptr = ptr.next
		new_node = Node(value)
		ptr.next = new_node
		self.size += 1

	# removes end item and returns its value
	def pop_back(self):
		ptr = self.head
		ptr2 = self.head.next
		while ptr2.next != None:
			ptr = ptr.next
			ptr2 = ptr2.next
		# now ptr is the last element
		# remove ptr2 and return its value
		ptr.next = None
		self.size -= 1
		return ptr2.data

	# get value of front item
	def front(self):
		return self.head.data

	# get value of end item
	def back(self):
		ptr = self.head
		while ptr.next != None:
			ptr = ptr.next
		return ptr.data

	# insert value at index, so current item at that index is pointed to by new item at index
	def insert(self, index, value):
		prev = None
		curr = self.head
		i = 0
		while i < index:
			prev = curr
			curr = curr.next
			i += 1
		# i is at index
		new_node = Node(value)
		if prev is not None:
			prev.next = new_node
		else:
			self.head = new_node
		new_node.next = curr
		self.size += 1

	# removes node at given index
	def erase(self, index):
		i = 0
		prev = None
		curr = self.head
		nxt = self.head.next
		while i < index:
			prev = curr
			curr = nxt
			nxt = nxt.next
			i += 1

		# delete curr
		if prev is not None:
			prev.next = nxt
		else:
			self.head = nxt
		self.size -= 1

	# returns the value of the node at nth position from the end of the list
	def value_n_from_end(self, n):
		ptr1 = self.head
		i = 0
		while i < n:
			ptr1 = ptr1.next
			i += 1
		ptr2 = self.head
		while ptr1 is not None:
			ptr1 = ptr1.next
			ptr2 = ptr2.next
		return ptr2.data

	# reverses the list
	def reverse(self):
		# x -> y -> z -> a -> b -> c
		prev = None
		curr = self.head
		while curr is not None:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt
		self.head = prev


	# removes the first item in the list with this value
	def remove_value(self, value):
		prev = None
		ptr = self.head
		while ptr is not None:
			if ptr.data == value:
				if prev is None:
					self.head = ptr.next
				else:
					prev.next = ptr.next
				break
			prev = ptr
			ptr = ptr.next

	# print values of linked list
	def print_vals(self):
		ptr = self.head
		while ptr is not None:
			print(ptr.data)
			ptr = ptr.next

x = LinkedList()
x.push_front(6)
x.push_back(7)
x.push_back(8)
x.push_back(7)


			

	
		




