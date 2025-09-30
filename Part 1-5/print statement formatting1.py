def formatted(my_list : float):

  change_list=[]    

  for numb in my_list:

    change_list.append(f"{numb:.2f}")
    # print(new_list)

  return change_list

my_list = [1.234, 0.3333, 0.11111, 3.446]
new_list = formatted(my_list)
print(new_list)