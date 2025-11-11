def line(numb,text):

 empty="*"
 if text=="":
     print(numb*empty)
 else:
     firstchar=text[0]
 
     print(firstchar*numb)


line(7, "%")
line(10, "LOL")
line(3, "")


2

def line(numb,text):

 empty="*"
 if text=="":
     print(numb*empty)
 else:
     firstchar=text[0]
 
     print(firstchar*numb)




def box_of_hashes(height):
 
 i=0
 
 text="#"
 
 while i<height:
     
     line(10,text)
     i+=1

box_of_hashes(5)
print()
box_of_hashes(2)

     



3

def line(numb,text):

 empty="*"
 if text=="":
     print(numb*empty)
 else:
     firstchar=text[0]
 
     print(firstchar*numb)




def square_of_hashes(length):
 
 i=0
 
 text="#"
 
 while i<length:
     
     line(length,text)
     i+=1

square_of_hashes(5)
print()
square_of_hashes(3)

4

def line(numb,text):

 empty="*"
 if text=="":
     print(numb*empty)
 else:
     firstchar=text[0]
 
     print(firstchar*numb)




def square(number, texts):
 
 i=0
 
 text="#"
 
 while i<number:
     
     line(number,texts)
     i+=1

square(5, "*")
print()
square(3, "o")