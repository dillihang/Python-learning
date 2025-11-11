def older_people(people: list, year: int):

    bunch_of_hags=[]

    for name in people:
        
        if name[1]<year:
            bunch_of_hags.append(name[0])

    return bunch_of_hags

        



def main():
  
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)

    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)

    print(older)

if __name__ == "__main__":

    main()
