string = input("please enter a string: ")

middle = "*"
end= "*"


while len(string) + len(middle) + len(end)<30:
    middle += " " 
    #if len(middle) + len(string) + len(end) < 30:
    end= " " + end


print("*" * 30)
print(middle + string + end)
print("*" * 30)





