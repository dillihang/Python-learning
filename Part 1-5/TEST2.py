let1 = input("Enter the first letter: ")
let2 = input("Enter the second letter: ")
let3 = input("Enter the third letter: ")

# Determine the middle letter using nested ifs
if let1 <= let2:
    if let1 >= let3:
        middle = let1
    else:
        if let2 <= let3:
            middle = let2
        else:
            middle = let3
else:
    if let1 <= let3:
        middle = let1
    else:
        if let2 >= let3:
            middle = let2
        else:
            middle = let3

print("The middle letter is:", middle)

 # Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order (NESTED).

# let1 = input("Enter the first letter: ")
# let2 = input("Enter the second letter: ")
# let3 = input("Enter the third letter: ")

# middle = sorted([let1, let2, let3])[1]  # middle letter
# print("The middle letter is:", middle)