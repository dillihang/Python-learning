import datetime
import string

def is_it_valid(pic:str):

    """Check if a Finnish Personal Identity Code (PIC) is valid.
    Validates the date, century marker, and control character.
    Returns True if all checks pass, otherwise False.
    """

    century_dict={"+":1800, "-":1900, "A":2000}
    controlstring="0123456789ABCDEFHJKLMNPRSTUVWXY"

    dd = int(pic[0:2])
    mm = int(pic[2:4])
    yy = int(pic[4:6])

   
    actual_year=century_dict[pic[6]]+yy

    try:
        datetime.datetime(actual_year, mm, dd)
        firststep = True
    except ValueError:
        firststep = False

    # print(firststep)

   
    if pic[6] in century_dict:

        secondstep=True
    else:
        secondstep=False

    # print(secondstep)

    result=""
    for i in pic[0:10]:
        if i in string.punctuation or i in string.ascii_letters:
            continue
        else:
            result+=i

    # print(result)
    
    int_result=int(result)//31
    final_result=int(result)-int_result*31

    if controlstring[final_result]==pic[10]:
        finalstep=True
    else:
        finalstep=False

    # print(finalstep)

    if firststep and secondstep and finalstep:

        valid=True
    else:
        valid=False

    return valid


if __name__=="__main__":

    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))

