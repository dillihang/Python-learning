def line(numb,text):

 empty="*"
 if text=="":
     print(numb*empty)
 else:
     firstchar=text[0]
 
     print(firstchar*numb)




def shape(numb,text,numb2,text2):
    i = 1
    
    while i <= numb:
        line(i, text)
        i += 1

    t=0

    while t<numb2:
       
       line(numb,text2)

       t+=1



shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")