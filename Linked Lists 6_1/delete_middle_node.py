from linked_list import LinkedList
from linked_list import Node
"""CCI 2.3: Delete Middle Node: Implement an algorithm to delete a node in the middle 
(any node but the first and last node, not necessarily the exact middle) of a singly linked list, 
given only access to that node. EXAMPLE Input: the node c from linked list a->b->c->d->e->f 
Result: nothing is returned but the new linked list looks like a->b->d->e->f"""

def delete_middle_node(node, ll):
	prev = None
	ptr = ll.head
	i = 0
	while ptr is not None:
		if ptr == node:
			nxt = ptr.next
			prev.next = nxt
			return
		else:
			prev = ptr
			ptr = ptr.next
			i += 1


x = LinkedList()
x.push_front(6)
x.push_back(7)
x.push_back(8)
x.push_back(7)

node_to_delete = x.head.next
delete_middle_node(node_to_delete, x)