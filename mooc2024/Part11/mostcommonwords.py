def most_common_words(filename: str, lower_limit: int):
    with open("part11/" + filename, "r") as file:
        new_string = "".join(line.strip().strip(".").replace(",", "") for line in file)
    part = new_string.split()
    return {word: part.count(word) for word in part if part.count(word)>=lower_limit}    

if __name__ == "__main__":

    print(most_common_words("comprehensions.txt", 3))