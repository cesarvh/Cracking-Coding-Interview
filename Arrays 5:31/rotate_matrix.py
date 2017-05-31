"""
CCI 1.7: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?

1 2 3 4
5 6 7 8
9 1 1 2
3 4 5 6

sol:
3 9 5 1
4 1 6 2
5 1 7 3
6 2 8 4
"""

def solution(matrix):
	# not in place
	n = len(matrix)
	sol_mtx = []
	for i in range(n):
		row = []
		for j in range(n):
			row.append(matrix[j][i])
		row = row[::-1] # lol this isn't that clear but it works because otherwise the row would be backwards
		sol_mtx.append(row)
	return sol_mtx


def solution2(matrix):
	# in place solution
	return