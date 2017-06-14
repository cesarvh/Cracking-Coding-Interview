class Stack():

    def __init__(self):
        self.size = 0
        self.min_element = float("-inf") 
        self.items = []
    
    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.items.append(item)
        self.size += 1
        if item < self.min_element:
            self.min_element = item 

    def pop(self):
        item = self.items[-1]
        del self.items[-1]
        self.size -= 1
        if item == self.min_element:
            self.min_element = min(self.items)
        return item
        
    def peek(self):
        return self.items[self.size - 1]

    def get_size(self):
        return self.size
    
    def print_stack(self):
        for i in range(1, self.size + 1):
            print (self.items[-i])
    
    def get_min(self):
        """
        How would you design a stack that has a function min() which
        returns the min element of a stack in O(1) time?
        """
        if self.min_element == float("-inf"):
            return None
        return self.min_element


class SetOfStacks():
    """
    Imagine a literal stack of plates. If it gets too high, it might topple.
    Therefore, IRL we would start a new stack when the previous stack
    exceeds some treshold. This is a data strcuture that mimics this. 
    SOS should be composed of several stacks and should create a new Stack
    once the Stack exceeds capacity. 
    """
    def __init__(self, capacity):
        self.stacks = {} 
        self.stack_sizes = {}
        self.size = 0
        self.capacity = capacity


    def push(self, item):
        if self.size == 0:
            # Initializing
            s = Stack()
            s.push(item)
            self.size += 1
            self.stacks[self.size] = s 
            self.stack_sizes[self.size] = s.get_size()
        else:
            if self.stack_sizes[self.size] == self.capacity:
                # create a new stack if at capacity
                new_stack = Stack()
                new_stack.push(item)
                self.size += 1
                self.stacks[self.size] = new_stack
                self.stack_sizes[self.size] = new_stack.get_size()
            else:
                # append to the current stack since its not full
                current_stack = self.stacks[self.size]
                current_stack.push(item)
                self.stacks[self.size] = current_stack
                self.stack_sizes[self.size] = current_stack.get_size()

    def pop(self):
        current_stack = self.stacks[self.size]
        item = current_stack.pop()
        # print (current_stack.print_stack())

        if current_stack.is_empty():
            # then remove it and decrease things woo
            del self.stacks[self.size]
            del self.stack_sizes[self.size] 
            self.size -= 1
        else:
            self.stacks[self.size] = current_stack
            self.stack_sizes[self.size] = current_stack.get_size()
        
        return item

    def peek(self):
        current_stack = self.stacks[self.size]
        return current_stack.peek()    
        


    def print_stacks(self):
        for k, v in sorted(self.stacks.items(), key=lambda x:x[0]):
             print ("Stack " + str(k))
             v.print_stack()
