import random
import string

def generate_strong_password(length: int, numb=False, special_char=False):
    """
    Generates a password of given length.
    - Always contains at least one lowercase letter.
    - If numb=True, at least one digit is included.
    - If special_char=True, at least one of !?=+-()# is included.
    """

    password=""
    new_punction="!?=+-()#"

    while True:

        for i in range(length):

            if not numb and not special_char:

                password+=random.choice(string.ascii_letters)

            elif numb and not special_char:
                letter=random.choice(string.digits)
                password+=letter

                letter=random.choice(string.ascii_letters + string.digits)
                password+=letter

            elif special_char and not numb:
                
                letter=random.choice(new_punction)
                password+=letter

                letter=random.choice(string.ascii_letters + new_punction)
                password+=letter

            else:

                letter=random.choice(string.digits)
                password+=letter
                letter=random.choice(new_punction)
                password+=letter

                letter=random.choice(string.ascii_letters + string.digits + new_punction)
                password+=letter

        
        passwordlist= list(password[0:length])

        random.shuffle(passwordlist)

        new_password="".join(passwordlist)
         

        counter = 0
        for char in new_password:


            if char in string.ascii_lowercase:
                counter+=1
                
        
        if counter > 0:
            return new_password
        
        else:
            password=""
            continue

    
if __name__=="__main__":

    for i in range(10):
        print(generate_strong_password(8, False, True))

   
    