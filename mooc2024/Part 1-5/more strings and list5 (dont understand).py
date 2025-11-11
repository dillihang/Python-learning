def longest_series_of_neighbours(my_list : list):

  print(my_list)
  
  neighbours = []
  current = [my_list[0]]

  for index in range(1, len(my_list)):

    test = my_list[index] - my_list[index-1]

    if test < 0:

      test = -1*test
    
    # range(my_list[index], my_list[index-1])
    if test==1:

      current.append(my_list[index])
    
    else:

      if len(current) > len(neighbours):

        neighbours = current[:]
      current = [my_list[index]]
  
  if len(current) > len(neighbours):

    neighbours = current[:]

  return len(neighbours)
      
      



if __name__ == "__main__":
# here the global variable is assigned
  my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
  print(longest_series_of_neighbours(my_list))