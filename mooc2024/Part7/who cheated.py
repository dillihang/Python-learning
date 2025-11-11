import datetime


def cheaters():
    """
    Identifies students who spent over 3 hours on any exam task.

    Reads 'start_times.csv' to get each student's exam start time
    and 'submissions.csv' to get the times of their task submissions.

    A student is considered a cheater if any of their submissions
    occurs more than 3 hours after their exam start time.

    Prints the names of students who cheated.
    """

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

            submission_dict[sub_part[0]]=[datetime.datetime(2025,1,1, hh, mm, 0)]
    
    for student, starttime in starttime_dict.items():
        if student in submission_dict:
            for submissiontime in submission_dict[student]:
                duration = submissiontime-starttime
                if duration > datetime.timedelta(hours=3):
                    print(f"{student} is a cheater")


if __name__=="__main__":

    cheaters()