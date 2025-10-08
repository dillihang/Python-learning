import string

def change_case(orig_string: str):

    newstring=""
    for word in orig_string:
        if word in string.ascii_lowercase:
            newword_case=word.upper()
            newstring+=newword_case
        elif word in string.ascii_uppercase:
            newword_case=word.lower()
            newstring+=newword_case    
        else:
            newstring+=word

    return newstring
        
def split_in_half(orig_string: str):

    length=len(orig_string)//2

    firsthalf=orig_string[:length]
    secondhalf=orig_string[length:]

    return(firsthalf),(secondhalf)

def remove_special_characters(orig_string: str):
    new_string=""

    for word in orig_string:
        if word in string.ascii_letters or word in string.digits:
            new_string+=word
        elif word == " ":
            new_string+=word
        else:
            continue


    return new_string

if __name__=="__main__":


    print(change_case("Well hello there!"))
    print(split_in_half("Well hello there!"))
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))