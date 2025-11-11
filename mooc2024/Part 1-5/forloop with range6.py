def distinct_numbers(my_list : list):

   my_list.sort()

   new_list = []

   for index in range(len(my_list)):
      
      if my_list[index]!= my_list[index-1]:
         new_list.append(my_list[index])
         

         
   return(new_list)

         # return my_list


my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) # [1, 2, 3]


