limit = int(input("Please enter the limit: "))
print("limit: " + str(limit))

total=0
i=1
calc= "The consecutive sum: "

while total<limit:
    total+=i
    
    if total==i:
        calc+= f"{i}"
    else:
        calc+= f" + {i}"  
    i+=1

print(f"{calc} = {total}")


# Ask the user for the limit and convert it to an integer.

# Print the entered limit so the user can see it.

# Initialize variables:

# total → running sum (starts at 0).

# i → current number to add (starts at 1).

# calc → string that will display the calculation.

# Start a while loop that runs while total is less than the limit.

# Inside the loop:

# Add i to total.

# Add i to calc to build the calculation string:

# If it’s the first number (total == i), add just the number.

# Otherwise, add " + " followed by the number.

# Increment i by 1 for the next iteration.

# After the loop finishes:

# Print calc with the final total so the output looks like The consecutive sum: 1 + 2 + 3 + 4 = 10.