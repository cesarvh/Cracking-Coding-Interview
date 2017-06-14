def palindrome_permutations(s):
    # TO DOOOOOO sry never finished this lol 
    s = s.replace(" ", "")
    mapping = {}

    for c in s:
        print (c)
        if s not in mapping:
            mapping[c] = 1
            continue
            
        if c in mapping:
            temp = mapping[c]
            temp += 1
            mapping[c] = temp
    counter = 0

    for key, value in mapping.items():
        if value == 1:
            counter += 1
    
    print (mapping)
    if counter > 1:
        return False
    return True
    
    # Cases:
    # 1. aaa
    # 2. abc
    # 3. abccba
    # 4. aabbcc
    # 5. acbac 





print (palindrome_permutations("cbbc"))
print (palindrome_permutations("aabc")) # counting as true, should be false
print (palindrome_permutations("abccba"))
print (palindrome_permutations("ccc"))
print (palindrome_permutations("abc"))
print (palindrome_permutations("abbcc"))
print (palindrome_permutations("aaa"))
print (palindrome_permutations("abc"))

    