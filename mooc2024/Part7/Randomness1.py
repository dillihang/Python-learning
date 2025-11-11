import random
import string

def generate_password(length: int):

    """Randomly generate password all lowercase"""

    password=""

    for i in range(length):

        password+=random.choice(string.ascii_lowercase)

    return password
    
if __name__=="__main__":

    for i in range(10):
        print(generate_password(8))