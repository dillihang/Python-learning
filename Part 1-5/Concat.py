Story = ""
prev = ""

while True:
    Word = input("Please type in words, type END to stop: ")
    Story += Word + " "
    if Word == "END" or Word == prev:
        break
    prev = Word
    
print(Story)

#repeated word makes while loop stop or END