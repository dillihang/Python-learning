def line(numb,text):

 empty="*"
 if text=="":
     print(numb*empty)
 else:
     firstchar=text[0]
 
     print(firstchar*numb)




def triangle(triang):
    i = 1
    while i <= triang:
        line(i, "#")
        i += 1



triangle(6)
print()
triangle(3)