def no_shouting(my_list : list):

  newlist= []

  for words in my_list:

    if words.isupper() is False:

      newlist.append(words)

  return(newlist)





if __name__ == "__main__":
# here the global variable is assigned
  my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
  pruned_list = no_shouting(my_list)
  print(pruned_list)