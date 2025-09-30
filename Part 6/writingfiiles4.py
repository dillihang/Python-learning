student_dict={}
exercise_dict={}
exam_dict={}
final_dict={}
courselist=[]
coursestring=""
resultlist=[]
finallist=[]

name_string=""



if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_data= input("Course information: ")
# else:
#     # hard-coded input
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"
#     exam_data="exam_points1.csv"


    if student_info =="students1.csv" and exercise_data=="exercises1.csv" and exam_data=="exam_points1.csv" and course_data=="course1.txt":

        with open("Part 6/students1.csv") as student_file:

            for students in student_file:
                
                students=students.replace("\n", "")
                parts=students.split(";")

                id=parts[0]
                name=parts[1:]

                name_string=name[0] + " " + name[1]

                student_dict[id]=name_string
        
        del student_dict["id"]
        


        with open("Part 6/exercises1.csv") as exercise_file:

            for exercises in exercise_file:

                exercises=exercises.replace("\n", "")
                exer_parts=exercises.split(";")
                exer_id=exer_parts[0]
                
                scores=exer_parts[1:]

                exercise_dict[exer_id]=scores

            
        
        del exercise_dict["id"]


        for keys,values in exercise_dict.items():
                int_list=[]
                for numbs in values:
                    int_list.append(int(numbs))
                exercise_dict[keys]=sum(int_list)



        with open("Part 6/exam_points1.csv") as exam_file:

            for points in exam_file:

                points=points.replace("\n", "")
                exam_parts=points.split(";")
                exam_id=exam_parts[0]
                exam_points=exam_parts[1:]
                if exam_id=="id":
                    continue

                exam_dict[exam_id]=exam_points



        for exam_keys,points_values in exam_dict.items():
                numb_list=[]
                for numbers in points_values:
                     numb_list.append(int(numbers))

                exam_dict[exam_keys]=sum(numb_list)


        with open("Part 6/course1.txt") as course_file:
             
             for data in course_file:
                  
                data=data.strip()
                datapart=data.split(":")  

                courselist.append(datapart[1].strip())
                     
 
        coursestring=f"{courselist[0]}, {courselist[1]} credits"
        

        for identification,total in student_dict.items():
            resultstring=""
            laststring=""
            
            if identification in exercise_dict and identification in exam_dict:

                newname=student_dict[identification]
                totalpoints=exercise_dict[identification]
                exampoints=exam_dict[identification]
                
                exerpercentage=(totalpoints/40*100)//10

                finalpoints=exampoints+exerpercentage

                if 0<=finalpoints<=14:
                     finalgrade=0
                elif 15<=finalpoints<=17:
                     finalgrade=1
                     
                elif 18<=finalpoints<=20:
                     finalgrade=2
                    
                elif 21<=finalpoints<=23:
                     finalgrade=3
                
                elif 24<=finalpoints<=27:
                     finalgrade=4
                
                elif finalpoints>=28:
                     finalgrade=5

                laststring+=f"{identification};{total};{finalgrade}"
                finallist.append(laststring)

            
            resultstring+=(f"{newname:30} {totalpoints:<10} {exerpercentage:<10.0f} {exampoints:<10} {finalpoints:<10.0f} {finalgrade:<10}")
            resultlist.append(resultstring)

    
 
        with open("Part 6/results.txt", "w" ) as write_file:
            write_file.write(f"{coursestring}\n")
            write_file.write(f"{len(coursestring)*"="}\n")
            write_file.write(f"name                           exec_nbr   exec_pts.  exm_pts.   tot_pts.   grade\n")
            for blah in resultlist:
                write_file.write(f"{blah}\n")
            


        with open("Part 6/results.csv", "w" ) as result_file:
             for items in finallist:
                  result_file.write(f"{items}\n")

        print("Results Written to files results.txt and results.csv")
             

        