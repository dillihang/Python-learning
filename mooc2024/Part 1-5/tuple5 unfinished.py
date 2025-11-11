def alphabet(alpha_dict: dict, alpha: str):

    for numb in range(1,(len(alpha)+1)):
        # print(f"{numb} : {alpha[numb-1]} ")

        alpha_dict[numb]=alpha[numb-1]
  

  
def printstars(alpha_dict: dict, times: int):

    print(f"Layers: {times}")
    height = times*2-1

    mylist=[]
    mystring=""
    mynew_string=""
    
    for numb, char in alpha_dict.items():
        heightstring=""
        if numb == times:
            mystring=(char*height)

            print(mystring)
            
            for index in range(height):
                print(f"this is index {index}")
                
                if index== 0:
                    mylist.append(mystring)

                elif index== height-1:
                    mylist.append(mystring)

                elif index ==1:
                    heightstring+=alpha_dict[times]+(alpha_dict[times-1]*(height-2))+alpha_dict[times]
                    mylist.append(heightstring)
                    
                
                elif index ==height-2:
                    heightstring=""

                    heightstring+=alpha_dict[times]+(alpha_dict[times-1]*(height-2))+alpha_dict[times]
                    mylist.append(heightstring)
                            

                    # middle index
                
                elif index== times-1:
                    y=times-1 

                    for char_index in range(len(mystring)):
                        
                        if char_index==0:
                            mynew_string+=alpha_dict[times]
                        
                        elif char_index== len(mystring)-1:
                            mynew_string+=alpha_dict[times]
                        
                        else:
                        
                            mynew_string+=alpha_dict[y]

                            if char_index<times-1:
                                y-=1
                            elif char_index>=times-1:
                                y+=1

                    mylist.append(mynew_string)

                # other index
                else:

                            
                    # middle rows except center
                    heightstring = ""
                    
                    # first character (outermost)
                    heightstring += alpha_dict[times]
                    
                    # decreasing letters toward middle
                    y = times - 1
                    for i in range(1, times - 1):
                        if i <= index:
                            heightstring += alpha_dict[y]
                            y -= 1
                        else:
                            y += 1
                            heightstring += alpha_dict[y]
                    
                    # increasing letters after middle
                    y = 2  # reset to start increasing toward edge
                    for i in range(times - 1, height - 1):
                        heightstring += alpha_dict[i]  # just to fill, adjust as needed
                    
                    # last character (outermost)
                    heightstring += alpha_dict[times]
                    
                mylist.append(heightstring)
                                    

                print(f"this is new string {mynew_string}")
                    

    
    print(mylist)



# FFFFFFFFFFF 0 1 sorted
# FEEEEEEEEEF 1 2 sorted  
# FEDDDDDDDEF 2 3 0
# FEDCCCCCDEF 3 4
# FEDCBBBCDEF 4 5
# FEDCBABCDEF 5 6	sorted
# FEDCBBBCDEF 6 7
# FEDCCCCCDEF 7 8
# FEDDDDDDDEF 8 9
# FEEEEEEEEEF 9 10 sorted
# FFFFFFFFFFF 10 11 sorted

# rules
                
                

    
def main():
    alpha_dict={}

    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet(alpha_dict, alpha)

    printstars(alpha_dict, 6)
    # printstars(alpha_dict, 4)
    # printstars(alpha_dict, 26)
    print()

    # printstars(4)
    
    # print(alpha_dict)
    # print(alpha_dict[14])

main()



# rules are :

# if numb==5 length and height is 7
# each time the value of length increases the values of height changes
# so height goes for numb==4
# 7*char
# 4444444 * 7
# 4333334
# (0123456)	
# 4322234
# 4321234 Till it reachers 4 then the reverse or it increases chars in legth of each height
# 4322234
# 4333334
# 4444444