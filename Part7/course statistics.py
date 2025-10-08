import urllib.request
import json

def retrieve_all():
    """
    Fetches all active courses from the University of Helsinki CS department API.

    Returns a list of tuples for each course that is currently enabled.
    Each tuple contains:
        (full course name, course code, year, total exercises)

    This function also prints the list of tuples in a visually formatted way,
    with each tuple on its own line and commas separating them.
    """

    result_list=[]

    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    web_json = my_request.read()

    data=json.loads(web_json)

    for items in data:
        if items['enabled']==True:  
            result_list.append((
                    items['fullName'], 
                    items['name'], items['year'], 
                    sum(items['exercises'])
                ))
           
    
    print("[")
    for details in range(len(result_list)):
        if result_list[details]== result_list[-1]:
            print(f"    {result_list[details]}")
        else:    
            print(f"    {result_list[details]},")

    print("]")


def retrieve_course(course_name: str):
    """
    Fetches weekly statistics for a specific course from the University of Helsinki CS department API.

    Parameters:
        course_name (str): The 'name' field of the course (e.g., "docker2019").

    Returns:
        dict: A dictionary containing aggregated statistics for the course, including:
            - 'weeks': Number of weeks of data
            - 'students': Maximum number of students in any week
            - 'hours': Total hours spent across all weeks
            - 'hours_average': Average hours per student (rounded down)
            - 'exercises': Total exercises completed across all weeks
            - 'exercises_average': Average exercises per student (rounded down)
    """
    
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats")
    web_json = my_request.read()

    data=json.loads(web_json)

    students_list=[]
    total_hours=0
    exercise_total=0

    
    for _,values in data.items():

        total_hours += int(values["hour_total"])
        exercise_total += int(values["exercise_total"])
        students_list.append(int(values["students"]))


    max_students=max(students_list)    
    average_hours=total_hours//max_students
    average_exercise=exercise_total//max_students
    total_weeks=len(data)

    course_dict = {
    'weeks': total_weeks,
    'students': max_students,
    'hours': total_hours,
    'hours_average': average_hours,
    'exercises': exercise_total,
    'exercises_average': average_exercise
    }

    return course_dict



if __name__=="__main__":

    # retrieve_all()

    new_dict=retrieve_course("docker2019")

    print('{')
    for names,numbs in new_dict.items():
        if names=="exercises_average":
            print(f"    '{names}': {numbs}")
        else:
            print(f"    '{names}': {numbs},")
    print('}')

    

    