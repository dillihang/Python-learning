def same_chars(word : str, index1 : int, index2 : int):

    if index2>len(word):

        return False

    if word[index1] == word[index2]:
        return True
    
    else:
        return False
    
print(same_chars("programmer", 6, 7)) # True

# different characters p and r
print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string
print(same_chars("programmer", 0, 12)) # False
    

