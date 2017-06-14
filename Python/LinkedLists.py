import math

class LinkedList():
    """
    Linked list class
    """

    size = 0
    tail = None #ALWAYS pointing to the last element!
    head = None

    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.size = 1

    def get_head(self):
        return self.head.value

    def empty(self):
        """
        Returns true if the list is empty
        """
        return self.size == 0

    def value_at(self, index):
        """
        Returns the value at @index
        """
        i = 0
        ptr = self.head
        while i != index:
            if ptr is None:
                return -1
            else:
                i += 1
                ptr = ptr.next
        return ptr.value

    def push_front(self, value):
        """
        Pushes new node to the front
        """
        new_node = Node(value)
        pointer = self.head 
        self.head = new_node
        new_node.next = pointer 
        self.size += 1

    def pop_front(self):
        """
        Removes item from the front and returns it
        """
        pointer = self.head
        self.head = pointer.next
        self.tail = pointer.next
        self.size -= 1
        return pointer
    
    def get_size(self):
        return self.size

    def push_back(self, value):
        """
        Appends item to the back
        """
        if self.size == 0:
            self.push_front(value)
            return
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    
    def push_node_back(self, node):
        if self.size == 0:
            self.head.next = node
            self.size += 1
        else:
            self.tail.next = node
            self.tail = node 
            self. size += 1

    def pop_back(self):
        """
        Removes the item at the tail and returns it
        """
        if self.size == 1:
            self.head = None
            self.size = 0
            return

        pointer = self.head
        while pointer.next != self.tail:
            pointer = pointer.next

        self.tail = pointer
        self.tail.next = None

        self.size -= 1

    def back(self):
        """
        Returns the item at the tail without removing it
        """
        return self.tail.value
    
    def front(self):
        """
        Returns the item at the head without removing it"
        """
        return self.head.value
    

    def insert(self, index, value):
        """
        Inserts @value at @index
        """
        i = 0
        pointer = self.head

        while i < index - 1:
            if pointer is None:
                raise IndexError("Index out of bounds at index" + str(index))
            pointer = pointer.next
            i += 1
        # pointer is now pointing to the insertion spot
        new_node = Node(value)
        new_node.next = pointer.next
        pointer.next = new_node
        self.size += 1
        return


    def remove(self, index):
        """
        Removes value @index
        """
        pointer = self.head
        i = 0
        while i < index - 1:
            if pointer is None:
                raise IndexError("Index out of bounds at index " + str(index))
            pointer = pointer.next
            i += 1
        pointer.next = pointer.next.next
        self.size -= 1

    def value_n_from_end(self, n):
        """
        Returns the nth value from the end
        """
        index = self.size - n - 1
        i = 0
        pointer = self.head
        while i != index:
            pointer = pointer.next
            if pointer is None:
                raise IndexError("Index out of bounds")
            i += 1
        return pointer.value

    def reverse(self):
        """
        Reverses the list
        """
        
        prev = None
        current = self.head
        nxt = current.next

        self.tail = self.head
        
        while nxt != None:
            current.next = prev
            prev = current
            current = nxt
            nxt = nxt.next

        self.head = current
        self.head.next = prev             
        
    def remove_value(self, value):
        """
        Removes all occurrences of @value in the list
        """
        pointer = self.head
        while pointer.next is not None:
            if pointer.next.value == value:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

    def print_list(self):
        """
        Prints the list in order
        """
        pointer = self.head
        while pointer != None:
            print (pointer.value)
            pointer = pointer.next

    def get_node(self, index):
        """
        Returns node at index
        """
        pointer = self.head
        i = 0 
        while i != index:
            pointer = pointer.next
            i += 1
        return pointer

class Node(object):
    """
    Node class
    """

    def __init__(self, value):
        self.value = value
        self.next = None


##### METHODS ######

def remove_duplicates(lst): # 2.1
    # Removes duplicates from an unsorted LinkedList
    # BUGGY :( Last elems remain the same
    seen = set()

    pointer = lst.head
    prev = None
    while pointer.next != None:
        if pointer.value not in seen:
            seen.add(pointer.value)
        else: # means its been seen, remove it
            prev.next = pointer.next

        prev = pointer
        pointer = pointer.next


def delete_middle_node(lst): #2.3
    # Deletes a node from the middle of a single linked list, given access to only this node
    pointer = lst.head
    i = 0 
    while i < int(lst.size / 2):
        pointer = pointer.next
        i += 1
    
    pointer.value = pointer.next.value
    pointer.next = pointer.next.next


def intersection(l1, l2): #2.7
    # Given two singly linked lists, determine if the two lists intersect 
    
    # Find the longer list
    ptr1 = l1.head
    ptr2 = l2.head
    if l1.get_size() > l2.get_size():
        steps = l1.get_size() - l2.get_size()
        for i in range(steps):
            ptr1 = ptr1.next
    elif l1.get_size() < l2.get_size():
        steps = l2.get_size() - l1.get_size()
        for i in range(steps):
            ptr2 = ptr2.next
    
    # now theyre the same woo
    while ptr1 is not None and ptr2 is not None:
        if ptr1 == ptr2:
            return True
        else:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
    return False

def oddEvenList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None or head.next is None or head.next.next is None):
            return head
        o = head
        e = head.next
        temp_e = e
        temp_o = o
        
        while e is not None and o is not None:
            if e.next is None or o.next is None:
                break
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next
        o.next = temp_e
        head = temp_o
        return head
