
def longest(strings : list):

    longest_string=[strings[0]]

    for words in strings:
        if len(words)>len(longest_string):

           longest_string = words

    return longest_string









if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
