from linked_list import LinkedList
from linked_list import Node

"""
2.7 Intersection: Given 2 singly linked lists, determine if the 2 lists intersect. 
Return the intersecting node. Not that the intersection is defined based on reference, not value. 
That is, if the kth node of the first linked list is the same node (by reference) as the jth node 
of the 2nd linked list, then they are intersecting.

  3 4 5 6
1 2 3 4 5

"""

# Algorithm: Get the length of the 2 linked lists. Set the longer linked list's starting point to the len-len2 index.
# Then, iterate.

def intersection(ll, ll2):
	len1 = ll.size - 1
	len2 = ll2.size - 1
	len1bigger = False
	if len1 > len2:
		diff = len1 - len2
		len1bigger = True
	else:
		diff = len2 - len1
	ptr1 = ll.head
	ptr2 = ll2.head
	if len1bigger:
		list1start = len2 - len1
		i = 0
		while i < list1start:
			ptr1 = ptr1.next
	else:
		list2start = len1 - len2
		i = 0
		while i < list2start:
			ptr2 = ptr2.next
	while ptr1 is not None and ptr2 is not None:
		if ptr1 == ptr2:
			return True
		ptr1 = ptr1.next
		ptr2 = ptr2.next

	return False

x = LinkedList()
x.push_front(6)
x.push_back(7)
x.push_back(8)
x.push_back(7)

intersect = x.head.next.next
y = LinkedList()
y.push_front(4)
y.push_back(5)
y.head.next.next = intersect
y.push_back(10)

z = LinkedList()
z.push_front(100)
z.push_back(99)








