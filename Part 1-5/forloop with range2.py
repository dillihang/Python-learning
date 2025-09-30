def list_of_stars(numbers : list):
    
    for stars in numbers:
        print(stars*"*")
    

list_of_stars([3, 7, 1, 1, 2])

print()
print()
print()

def anagrams(word1 : str, word2 : str):
    
   if sorted(word1) == sorted(word2):
      return True
   else:
        return False


print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False


print()
print()
print()


def palindromes(inputword : str):

   listedinputword = list(inputword)
   listedinputword2= list(inputword)
   print(listedinputword2)

   listedinputword.reverse()
   

   reverseword=listedinputword
   print(reverseword)

      
   if reverseword == listedinputword2:
        
      return True
   else:
      return False

while True:
    
   inputword = input("Please type in a palindrome: ")

   if palindromes(inputword) is  True:
      print(f"{inputword} is a palindrome!")
      break
   else:
      print(f"that wasn't a palindrome!")

   
    

