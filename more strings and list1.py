def everything_reversed(my_list : list):

  reversedwords=[]

  for words in my_list: 
    reversedwords.append(f"{words[-1::-1]}")
    # print(reversedwords)

  return reversedwords[-1::-1]



mylist = [1,2,3]
mylist[0] = 10
print(mylist)

my_string = "Hey"
my_string = my_string + "!"
print(my_string)

my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
print(my_string.count("ch"))

my_list = [1,2,3,1,4,5,1,6]
print(my_list.count(1))

my_string = "Hi there"
new_string = my_string.replace("Hi", "Hey")
print(new_string)

sentence = "sheila sells seashells on the seashore"
print(sentence.replace("she", "SHE"))




if __name__ == "__main__":
# here the global variable is assigned
  my_list = ["Hi", "there", "example", "one more"]
  new_list = everything_reversed(my_list)
  print(new_list)