def list_sum(a : list, b : list):

   sumlist=[]
   for i in range(len(b)):
      sumlist.append(a[i]+b[i])
   
   return(sumlist)
      
      

a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 10, 12]


