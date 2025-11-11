def first_word(sentence : str):

    firstspaceindex=sentence.find(" ")

    firstword = sentence[0:firstspaceindex]
    return firstword
    
    
def second_word(sentence : str):

    firstspaceindex=sentence.find(" ")

    tempsentence = sentence[firstspaceindex+1:]
    # print(tempsentence)

    secondspaceindex=tempsentence.find(" ")

    secondword=tempsentence[0:secondspaceindex]

    return secondword

def last_word(sentence : str):

    
    pos=0
    tempsentence=sentence

    while pos<len(tempsentence):
        findlastindex=tempsentence.find(" ", pos)

        if findlastindex==-1:
            break

        print(findlastindex)

        pos+=1
        

        lastindex=findlastindex

    # print(lastindex)

    lastword=sentence[lastindex+1:]
    # print(lastword)
    return lastword



def secondlast_word(sentence : str):

    
    pos=0
    tempsentence=sentence

    while pos<len(tempsentence):
        findsecondlastindex=tempsentence.find(" ", pos)

        if findsecondlastindex==-1:
            break

        print(findsecondlastindex)

        pos+=1
        

        secondlastindex=findsecondlastindex

    # print(lastindex)

    lastword=sentence[secondlastindex+1:]
    # print(lastword)
    return lastword


sentence = "HELLO DARKNESS MY OLD FRIEND"

print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python
print(secondlast_word(sentence)) # python