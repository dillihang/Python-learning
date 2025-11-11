def oldest_person(people: list):

    """original version"""

    # all_age=[]
    # lowest_age=0
    
    # for name in range(len(people)):
    #     for age in range(len(people[name])):

    #         if age==1:

    #             all_age.append(people[name][age])
    
    # lowest_age=min(all_age)
    
    
    # for name in range(len(people)):
    #     if lowest_age in people[name]:
    #         return (people[name][0])

    """compressed version"""

    oldest= people[0][1]

    for name in  people:

        
        if oldest > name[1]:
            oldest=name[1]
            oldestname=name[0]
            # print(oldest)

    return oldestname
    
        



def main():
  
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1963)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)

    people = [p1, p2, p3, p4]

    print(oldest_person(people))

if __name__ == "__main__":

    main()
