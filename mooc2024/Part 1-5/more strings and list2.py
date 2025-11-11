def most_common_character(first_string : str):

  savingcounters = []


  for char in first_string:

    savingcounters.append(first_string.count(char))

  for char in first_string:
    

    if  first_string.count(char) == max(savingcounters):
      return char
      


if __name__ == "__main__":
# here the global variable is assigned
  first_string = "abcdbde"
  print(most_common_character(first_string))

  second_string = "exemplaryelementary"
  print(most_common_character(second_string))