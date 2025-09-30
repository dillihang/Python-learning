def no_vowels(my_string : str):

  index = 0
  new_string = ""
  vowels = "aeiou"

  while index < len(my_string):

    if my_string[index] not in vowels:


      new_string += my_string[index]
  
    
    index+=1

  return new_string
    
      
      


if __name__ == "__main__":
# here the global variable is assigned
  my_string = "this is an example"
  print(no_vowels(my_string))