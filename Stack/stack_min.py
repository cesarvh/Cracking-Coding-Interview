"""
How would you design a stack which, in addition to push and pop, has a function min which returns the
minimum element? Push, pop, and min should all operate in O(1) time.

stack:
5
1
4
2
9

min stack:
1
1
2
2
9
"""

class Stack:
	def __init__(self):
		self.nums = []
		self.mins = []
		self.size = 0
		# mins is also a "stack"

	def push(self, num):
		self.nums.append(num)
		if self.mins == []:
			self.mins.append(num)
		else:
			curr_min = self.mins[self.size - 1]
			if num < curr_min:
				self.mins.append(num)
			else:
				self.mins.append(curr_min)
		self.size += 1
		return num

	def pop(self):
		num = self.nums.pop()
		self.mins.pop()
		self.size -= 1
		return num

	def minimum(self):
		return self.mins[self.size - 1]

x = Stack()
x.push(1)


