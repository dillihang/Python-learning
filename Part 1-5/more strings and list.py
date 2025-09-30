my_string = "exemplary"
print(my_string[0:7:2])
my_list = [1,2,3,4,5,6,7,8]
print(my_list[6:2:-1])


print()
print()
print()

def print_reversed(names: list):
    # using the global variable instead of the parameter by accident
    i = len(name_list) - 1
    while i >= 0:
        print(name_list[i])
        i -= 1


if __name__ == "__main__":
# here the global variable is assigned
  name_list = ["Steve", "Jean", "Katherine", "Paul"]
  print_reversed(name_list)
  print()
  print_reversed(["Huey", "Dewey", "Louie"])



print()
print()
print()

# FIXED VERSION

def print_reversed(names: list):
    # using the global variable instead of the parameter by accident
    i = len(names) - 1
    while i >= 0:
        print(names[i])
        i -= 1



if __name__ == "__main__":
# here the global variable is assigned
  name_list = ["Steve", "Jean", "Katherine", "Paul"]
  print_reversed(name_list)
  print()
  print_reversed(["Huey", "Dewey", "Louie"])
