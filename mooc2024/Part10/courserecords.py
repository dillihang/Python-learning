import statistics
from collections import Counter

class Course:
    """
    Course Study Tracker Application

    This program allows the user to keep track of their study courses, grades, and credits. 
    Users can interactively add courses, update grades (ensuring grades only increase), 
    retrieve course information, and view overall statistics.

    Classes:
    - Course: Represents a single course with a name, grade, and credits.
    - CourseDatabase: Manages a collection of Course objects. Handles adding course 
    details, retrieving course data, calculating total credits, average grade, and 
    grade distribution.
    - CourseApp: Provides a command-line interface for the user to interact with the 
    CourseDatabase. Supports adding courses, searching courses, viewing statistics, 
    and exiting the program.

    Features:
    - Adding a new course with grade and credits.
    - Updating course grade only if it increases.
    - Retrieving course details.
    - Displaying statistics:
        - Total completed courses
        - Total credits
        - Mean grade
        - Grade distribution from 5 to 1 with visual "x" markers.

    Grade distribution has been implemented in two ways:
    1. Using the `Counter` module (currently commented out) to count occurrences of 
    each grade and convert counts to "x" symbols.
    2. Using a beginner-friendly approach by initializing a dictionary with keys 1–5 
    and iterating through courses to append "x" to the corresponding grade. This 
    is the version currently in use.
    """
    def __init__(self, name: str):
        self.__name = name
        self.__grade = None
        self.__credits = None
    
    def name(self):
        return self.__name
    
    def grade(self):
        return self.__grade
    
    def credits(self):
        return self.__credits
    
    def add_grade(self, grade: int):
        self.__grade = grade
    
    def add_credit(self, credits: int):
        self.__credits = credits
    
    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"
    
class CourseDatabase:
    def __init__(self):
        self.__courses = {}

    def add_course_details(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            new_course_object = Course(name)
            new_course_object.add_grade(grade)
            new_course_object.add_credit(credits)
            self.__courses[name]=new_course_object
        else:
            existing_course = self.__courses[name]
            if existing_course.grade()<grade:
                existing_course.add_grade(grade)

    def get_course_data(self, name):
        if name in self.__courses:
            return self.__courses[name]
        
    def get_credits_total(self):
        totalcredits = 0
        for names, course_objects in self.__courses.items():
            totalcredits += course_objects.credits()
        
        return totalcredits
    
    def get_total_courses(self):
        return len(self.__courses)
    
    def get_grade_average(self):
        grade_list = []
        for names, course_objects in self.__courses.items():
            grade_list.append(course_objects.grade())
        
        return statistics.mean(grade_list)
    
    def get_grade_distribution(self): 
        # grade_dict = {}
        # mark = "x"
        # i=1
        # grade_list = []

        # for names, course_objects in self.__courses.items():
        #     grade_list.append(course_objects.grade())

        # count = Counter(grade_list)
        
        # for items, values in count.items():
        #     count[items]=values*mark

        # while i<=5:
        #     if i in count:
        #         grade_dict[i] = count[i]
        #     else:
        #         grade_dict[i] = None
        #     i+=1
        # reversed_dict = dict(reversed(grade_dict.items()))
        # return reversed_dict
    
        grade_dict = {1: "", 2: "", 3: "", 4: "", 5: ""}

        for items, values in self.__courses.items():
            grade_dict[values.grade()] += "x"
        

        reversed_dict = dict(reversed(grade_dict.items()))
        return reversed_dict
    
class CourseApp:
    def __init__(self):
        self.__coursedatabase = CourseDatabase()

    def instructions(self):
        print("commands:")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def adding_course(self):
        name = input("Course: ")
        grade = int(input("Grade: "))
        credits = int(input("Credits: "))
        self.__coursedatabase.add_course_details(name, grade, credits)
    
    def search_by_course_name(self):
        course_name = input("Course: ")
        course_object = self.__coursedatabase.get_course_data(course_name)
        if course_object:  
            print(course_object)
        else:
            print("no entry for this course")

    def print_statistics(self):
        print(f"{self.__coursedatabase.get_total_courses()} completed courses, a total of {self.__coursedatabase.get_credits_total()} credits")
        print(f"mean {self.__coursedatabase.get_grade_average()}")
        print("grade distribution")
        for keys, values in self.__coursedatabase.get_grade_distribution().items():
            if values == None:
                print(f"{keys}: ")
            else:
                print(f"{keys}: {values}")
            
    def execute(self):
        self.instructions()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.adding_course()
            elif command == "2":
                self.search_by_course_name()
            elif command == "3":
                self.print_statistics()
            else:
                self.instructions()
        
if __name__ == "__main__":

    app = CourseApp()
    app.execute()


    


