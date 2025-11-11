def even_numbers(my_list : list):
    
   newlist=[]

   for numb in my_list:
      if numb%2==0:
         newlist.append(numb)

   # print(my_list)
   return newlist


my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)


def list_sum(a : list, b : list):

   sumlist=[]
   for i in range(len(b)):
      sumlist.append(a[i]+b[i])
   
   return(sumlist)
      
      

a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 10, 12]