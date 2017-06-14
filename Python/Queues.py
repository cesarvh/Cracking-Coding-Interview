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
        
        # reversed!

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
        pass
    
    def dequeue(self):
        pass
    
    def empty(self):
        return self.size == 0
    

class ArrayQueue():

    def __init__(self):
        self.size = 0
        self.items = []
    
    def enqueue(self, item):
        pass
    
    def dequeue(self):
        pass
    
    def empty(self):
        pass 
    
    def full(self):
        pass 