import string

def separate_characters(my_string: str):

    first_string=""
    second_string=""
    third_string=""

    for i in my_string:

        if i in string.ascii_letters:
            first_string+=i
        elif i in string.punctuation:
            second_string+=i
        else:
            third_string+=i


    return (first_string, second_string, third_string)
            


if __name__=="__main__":

    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])