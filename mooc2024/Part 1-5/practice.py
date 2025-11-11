my_list=[1,2,3,4,5]

newbox= []

for index in range(len(my_list)):
    # print(my_list[index])
    for number in range(len(my_list)):
       
       newbox.append(my_list[index]*my_list[number])

print(newbox)

my_list = [1, 2, 3, 4, 5]

for i in my_list:
    for j in my_list:
        print(i * j, end=" ")
    print()  # moves to next row



mynew_list=[12, 33, 24, 41, 8, 19]

for numbs in mynew_list:
    if numbs > 20:
        print(numbs)


char_list=['a', 'b', 'c', 'd']

for index in range(len(char_list)):

    print(f"{index}: {char_list[index]}")



word = "experience"
counter = 0

for char in word:
    if char == "e":
        counter += 1  # add 1 each time we see 'e'

print(counter)

counter=word.count("e")
print(counter)



stars="*"

for i in range(1,6):
    print(stars*i)


string="abcdefg"

c="c"

for char in range(len(string)):
    if string[char] == c:
        print(string[char:char+3])
    
        
    