wordlist = []

while True:

    word = input("Word: ")

    if word in wordlist:

        print(f"You typed in {len(wordlist)} different words")
        print(wordlist)

        break

    wordlist.append(word)