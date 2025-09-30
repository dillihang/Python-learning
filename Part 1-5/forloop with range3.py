def sum_of_positives(my_list : list):
    
   for i in range(len(my_list)):
      
      if my_list[i] < 0:
         my_list[i] = my_list[i] - my_list[i]*2
      
   print(my_list)  
   return sum(my_list)         
      
            
my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)    


def sum_of_positives(my_list : list):

   for numb in my_list:
      if numb<0:
         my_list.remove(numb)

   print(my_list)
   return sum(my_list) 


my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)