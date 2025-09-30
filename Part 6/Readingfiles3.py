student_dict={}
exercise_dict={}

name_string=""



while True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")


    if student_info =="students1.csv" and exercise_data=="exercises1.csv":

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



        for identification,total in student_dict.items():

            if identification in exercise_dict:

                newname=student_dict[identification]
                totalpoints=exercise_dict[identification]

                print(f"{newname} {totalpoints}")


        



                

           

            # del id_list[0]
            # del myexer_list[0]

            # print(id_list)
        
            
            # 

            # myexer_list=converted

            # print(myexer_list)


                


                





       


            

        
    

            



    