def dict_of_numbers():

    somedict={0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
              11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 
              19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    
    
    finaldict={}
    

    i=21
    t=1
    f=20
    while i <= 99:
        
        if i in (30, 40, 50, 60, 70, 80, 90):
            i += 1

        finaldict[i]= somedict[f]+ "-" + somedict[t]
        
        if t==9:
            t=0
            
            f+=10
            
        
        t+=1
        i+=1

    """forloop version by chatgpt"""

    # finaldict = dict(somedict)

    # for i in range(21, 100):
    #     if i in (30,40,50,60,70,80,90):
    #         continue

    #     f = (i // 10) * 10
    #     t = i % 10
    #     finaldict[i] = somedict[f] + "-" + somedict[t]

    

    for key,value in somedict.items():

        finaldict[key]=value


    return(finaldict)
        



def main():
  
   numbers = dict_of_numbers()
   print(numbers[2])
   print(numbers[11])
   print(numbers[45])
   print(numbers[99])
   print(numbers[0])

if __name__ == "__main__":

    main()





    