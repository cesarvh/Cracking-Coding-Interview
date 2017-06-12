"""
CCI 1.4: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards
and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

Ex

Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc)
"""

def solution(s):
	# true if no odd count or only 1 odd count
	# Tact Coa -> get rid of spaces and change to lower case tactcoa
	s = s.replace(" ", "")
	s = s.lower()
	if s == "":
		return True
	char_to_count = {}
	for i in range(len(s)):
		c = s[i]
		if c not in char_to_count:
			char_to_count[c] = 1
		else:
			char_to_count[c] += 1
	num_odd = 0
	for char in char_to_count:
		if char_to_count[char] % 2 != 0:
			num_odd += 1
		if num_odd > 1:
			return False
	return True


