import random

def words(n: int, beginning:str):

    """
    Return a list of n unique random words from words.txt that start with the given prefix.
    Raises a ValueError if there aren't enough matching words.
    """

    my_list=[]
    

    with open("Part7/words.txt") as file:

        for line in file:
            line=line.strip()

            if line.startswith(beginning):
                if line not in my_list:
                    my_list.append(line)
        
    
    if len(my_list)<n:

        raise ValueError
    else:

        words = random.sample(my_list, n)

        return words
            

if __name__=="__main__":

    word_list = words(3, "ca")
    for word in word_list:
        print(word)
    