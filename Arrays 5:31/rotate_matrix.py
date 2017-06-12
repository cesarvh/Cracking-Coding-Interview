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

"""
1 2 3 4 5
6 7 8 9 0
2 3 4 5 6
7 6 5 4 3
2 4 6 8 9

If odd, still 2 cycles, 1 middle number stays the same
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
	# in place solution, cri this doesn't work i need to rethink 
	n = len(matrix)
	num_cycles = n // 2
	for i in range(num_cycles):
		# first cycle
		count = 0
		for j in range(i, n - i): # rn just rotate first layer, 2nd layer: 1 to 3, i = 1
			row1num = matrix[i][i + count] # 1 2 3 4 ||  6
			colnnum = matrix[j][n - 1 - i] # 4 8 2 6 ||  7
			rownnum = matrix[n - 1 - i][n - 1 - i - count] # 6 5 4 3 ||  1
			col1num = matrix[n - 1 - i - count][i] # 3 9 5 1 || 
			count += 1
			print(i, j, count)
			# rotate here
			matrix[i][i + count] = col1num
			matrix[j][n - 1 - i] = row1num
			matrix[n - 1 - i][n - 1 - i - count] = colnnum
			matrix[n - 1 - i - count][i] = rownnum

	return matrix

x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 1, 2], [3, 4, 5, 6]]