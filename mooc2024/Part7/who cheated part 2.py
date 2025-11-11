import datetime


def final_points():
    """
    Calculates each student's total valid exam points.

    Reads start times and submissions from CSV files.
    For each task, only the best (highest-scoring) submission
    made within 3 hours of the student's start time is counted.

    Returns:
        dict: {student_name: total_points}
    """

    final_points_dict={}
    starttime_dict={}
    submission_dict={}

    with open("part7/start_times.csv") as file:
        for line in file:

            line=line.strip()
            part=line.split(";")
            part1=part[1]
            time_hhmm=part1.split(":")

            time_hh=int(time_hhmm[0])
            time_mm=int(time_hhmm[1])

            
            starttime_dict[part[0]]=datetime.datetime(2025,1,1, time_hh, time_mm, 0)
            

    with open("part7/submissions.csv") as new_file:
        for items in new_file:

            items=items.strip()
            sub_part=items.split(";")
            sub_part1=sub_part[3]
            sub_hhmm=sub_part1.split(":")
            hh=int(sub_hhmm[0])
            mm=int(sub_hhmm[1])
            tasks=int(sub_part[1])
            stu_points=int(sub_part[2])
            studentname=sub_part[0]

            """NESTED DICTIONARY!!!!!"""

            if studentname not in submission_dict:
                    submission_dict[studentname] = {} 
            if tasks not in submission_dict[studentname]:
                submission_dict[studentname][tasks]=[datetime.datetime(2025,1,1, hh, mm, 0), stu_points]

            else:
                if stu_points>submission_dict[studentname][tasks][1]:
                    submission_dict[studentname][tasks][1] = stu_points
                    submission_dict[studentname][tasks][0] = datetime.datetime(2025,1,1, hh, mm, 0)  
                      
                
    for student, tasks in submission_dict.items():
        starttime = starttime_dict[student]
        for task_number, value in tasks.items():
            submission_time = value[0]
            points = value[1]
            duration = submission_time - starttime

            if duration <= datetime.timedelta(hours=3):
                if student not in final_points_dict:
                    final_points_dict[student] = 0
                final_points_dict[student] += points

    return final_points_dict


if __name__=="__main__":

    print(final_points())