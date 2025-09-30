userlist=[]

print(userlist)

item = int(input("How many items: "))

index=1

while index<=item:

    items=int(input(f"Item {index}: "))
    userlist.append(items)

    index+=1

print(userlist)