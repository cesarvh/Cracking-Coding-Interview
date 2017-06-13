"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we
would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure
SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once 
the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single
stack (that is, pop() should return the same values as it would if there were just a single stack)

FOLLOWUP: Implement a function popAt(int index) which performs a pop operation on a specific sub-stack

"""

class SetOfStacks:
	# n is the threshold
	def __init__(self, n):
		self.stacks = [] # array of stacks
		self.num_stacks = 0
		self.t = n

	def push(self, num):
		if self.stacks == []:
			self.stacks.append([])
			self.num_stacks += 1
		curr_stack = self.stacks[self.num_stacks - 1]
		if len(curr_stack) == self.t:
			# make a new stack and put it on there
			new_stack = []
			self.stacks.append(new_stack)
			self.num_stacks += 1
			new_stack.append(num)
		else:
			curr_stack.append(num)
		return num

	def pop(self):
		if self.stacks == []:
			return
		curr_stack = self.stacks[self.num_stacks - 1]
		if len(curr_stack) == 1:
			num = curr_stack.pop()
			self.stacks.pop()
			self.num_stacks -= 1
		else:
			num = curr_stack.pop()
		return num

	def popAt(self, index): # index specifies which stack
		stack = self.stacks[index]
		return stack.pop()

x = SetOfStacks(3)
x.push(1)
x.push(2)
x.push(3)
x.push(4)
x.push(5)
x.push(6)
x.push(7)
