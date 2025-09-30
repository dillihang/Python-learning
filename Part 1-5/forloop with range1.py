number = int(input("Please type in a positive integer: "))

mylist=[]

for i in range(-number, number):

   mylist.append(i)

# print(mylist)

mylist.remove(0)
mylist.append(number)

# print(mylist)

for num in mylist:
   print(num)



number = int(input("Please type in a positive integer: "))

for i in range(-number, number+1):
   
   if i!=0:
      print(i)