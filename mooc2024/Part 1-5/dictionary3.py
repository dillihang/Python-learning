def histogram(words: str):

    dis={}
    counter=0
    countedwords=""
    stars="*"
    for char in words:

        counter=words.count(char)
        if char not in countedwords:
            # countedwords+=char
            # countedwords+=stars*counter
            dis[char]=stars*counter

    
    for key, value in dis.items():
        print(f"{key} {value}")
        


if __name__ == "__main__":

    histogram("abba") 
    print()
    histogram("statistically")

    