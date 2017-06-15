from LinkedLists import LinkedList, Node

class QueueOfStacks(object):
    # Leetcode 232
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        self.size += 1
    
    def reverse(self):
        if len(self.stack2) == 0:
            for item in self.stack1:
                self.stack2.append(item)
            self.stack1 = []
        else:
            for item in self.stack2:
                self.stack1.append(item)
            self.stack2 = []

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.reverse()
        element = self.stack2[0] #grab element
        del self.stack2[0]
        self.reverse()
        self.size -= 1
        return element
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.reverse()
        item = self.stack2[0]
        self.reverse()
        return item
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.size == 0
        

class LinkedListQueue():

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def dequeue(self):
        item = self.head.value
        self.head = self.head.next
        self.size -= 1
        return item
    
    def empty(self):
        return self.size == 0
    
    def print_queue(self):
        pointer = self.head
        while pointer is not None:
            print (pointer.value)
            pointer = pointer.next
    

class ArrayQueue():

    def __init__(self, limit):
        self.size = 0
        self.items = []
        self.limit = limit

    def enqueue(self, item):
        if self.full():
            raise Exception("The queue is full")
        else:
            self.size += 1
            self.items.append(item)

    
    def dequeue(self):
        item = self.items[0]
        del self.items[0]
        return item
    
    def empty(self):
        return self.size == 0
    
    def full(self):
        return self.size == self.limit
    
    def print_queue(self):
        for i in range(self.size):
            print self.items[i]

