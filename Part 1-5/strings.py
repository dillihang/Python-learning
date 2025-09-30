firsts = input("first String please: ")
seconds = input("second string please: ")

if len(firsts) >= len(seconds):
    if len(firsts) == len(seconds):
        print(f"The strings are equally long")
    else:
        print(f"{firsts } is longer")
            
else:
    print(f"{seconds } is longer")

    
    