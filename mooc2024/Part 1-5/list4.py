thelist = []

while True:

    item = int(input("New item: "))
    if item == 0:
        break
    thelist.append(item)
    print(f"The list now: {thelist}")
    print(f"The list in order: {sorted(thelist)}")

    

