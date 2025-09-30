

limit = int(input("Please enter the limit: "))

print("Limit: " + str(limit))

total=0
i=1
while total < limit:
    total+=i

    i+=1

print(total)



# Iteration breakdown for limit = 10:

# First iteration

# i = 1

# total = total + i = 0 + 1 = 1 ✅

# i is incremented: i = 2

# Second iteration

# i = 2

# total = total + i = 1 + 2 = 3 ✅

# i is incremented: i = 3

# Third iteration

# i = 3

# total = total + i = 3 + 3 = 6 ✅

# i is incremented: i = 4

# Fourth iteration

# i = 4

# total = total + i = 6 + 4 = 10 ✅

# i is incremented: i = 5

# Now total = 10, which is not less than 10, so the while loop ends.    
    
    
    


