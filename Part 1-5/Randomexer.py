while True:

    editor=input("What editor do you use? ")

    editor=editor.lower()


    if editor=="visual studio code":
        print("an exellent choice!")
        break

    
    if editor=="notepad" or editor=="word":
        print("awful")
    else:
        print("not good")
    
