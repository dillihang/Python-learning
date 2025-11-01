from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.credits = credits
        self.grade = grade
    
    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(course_list: list):
    return reduce(lambda total, item : total+item.credits, course_list, 0)

def sum_of_passed_credits(course_list: list):
    new_list = list(filter(lambda course: course.grade >=1, course_list))
    return reduce(lambda total, item: total+item.credits, new_list, 0)

def average(course_list: list):
    new_list = list(filter(lambda course: course.grade >=1, course_list))
    return reduce(lambda grade_total, item: grade_total + item.grade, new_list, 0)/len(new_list)


if __name__=="__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)