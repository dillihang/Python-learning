class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade
    
    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
    

def names_of_students(attempts: list):
    return list(map(lambda name: name.student_name, attempts))

def course_names(attempts: list):
    new_list = set(list(map(lambda name: name.course_name, attempts)))

    def order_by_course(item: "CourseAttempt"):
        return item[1]

    return sorted(new_list, key=order_by_course)

def accepted(attempts: list):
    return list(filter(lambda info: info.grade >=1, attempts))

def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda info: info.grade == grade, attempts))

def passed_students(attempts: list, course: str):
    new_list = list(filter(lambda info: info.course_name == course and info.grade >=1, attempts))
    return sorted(map(lambda name: name.student_name, new_list))

if __name__=="__main__":
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)