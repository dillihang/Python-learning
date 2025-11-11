def create_tuple(x: int, y: int, z: int):

    tuplist=[x,y,z]

    smallest = min(tuplist)
    biggest = max(tuplist)
    total = sum(tuplist)



    tup=(smallest,biggest,total)

    return tup




    


def main():
  
   print(create_tuple(5, 3, -1))

if __name__ == "__main__":

    main()
