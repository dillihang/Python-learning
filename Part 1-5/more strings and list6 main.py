# Helper function: finds the longest series of neighbours
def longest_series_of_neighbours(my_list: list):
    current = [my_list[0]]  # start with first element
    neighbours = []          # longest sequence found so far

    for index in range(1, len(my_list)):
        test = my_list[index] - my_list[index - 1]
        if test < 0:
            test = -1 * test  # absolute difference

        if test == 1:
            # numbers are neighbours → add to current sequence
            current.append(my_list[index])
        else:
            # sequence breaks → check if current is the longest
            if len(current) > len(neighbours):
                neighbours = current[:]
            current = [my_list[index]]  # start new sequence

    # check last sequence at the end
    if len(current) > len(neighbours):
        neighbours = current[:]

    return neighbours


# Main function: sets up data and calls the helper
def main():
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print("Input list:", my_list)

    # Call the helper function
    result = longest_series_of_neighbours(my_list)

    # Show the result
    print("Longest series of neighbours:", result)


# Run the main program
main()

print(longest_series_of_neighbours([1,2,3,2,1]))
print(longest_series_of_neighbours([5,4,3,2,1]))