import statistics

def add_student(students: dict, stu_names: str):
    
    emptylist=[]

    students[stu_names]=emptylist


def add_course(students: dict, stu_names: str, courses: tuple):

  
    if courses[1] != 0:
       
        students[stu_names].append(courses)
    

        
def print_student(students: dict, stu_names: str):

    totalpoints=[]

    uniquecourse={}

    if stu_names not in students:

        print(f"{stu_names}: no such person in the database")
    #
    elif students[stu_names]==[]:

        print(stu_names)
        print("no completed courses")

    else:      
        print(f"{stu_names}:")
        print(f"{len(students[stu_names])} completed courses: ")

        for course, number in students[stu_names]: 
            print(f" {course} {number}")

            if course not in uniquecourse:
                uniquecourse[course]=number
            
            else:
                if number>uniquecourse[course]:
                    uniquecourse[course]=number
        # print(uniquecourse)

        for keys,value in uniquecourse.items():

            totalpoints.append(value)


        print(f"average grade {statistics.mean(totalpoints):.1f}")    
            
        print()


def summary(students: dict):

    finaldict={}
    dist={}

    
    print(f"students {len(students)}")

   
    for keys,values in students.items():

        print(keys)
        print(values)
        finaldict[keys]=(len(students[keys]))

       

    print(f"most course completed {finaldict[max(finaldict)]} {max(finaldict)}")

    
    


def main():

    students = {}
  
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("test course", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    add_course(students, "Peter", ("Introduction to Programming", 4))
    add_student(students, "Eliza")
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    print()
    print()
    print()
    summary(students)

    print()
    print()
    print()
    

    

if __name__ == "__main__":

    main()
