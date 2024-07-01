class Student:
    
    # constructor
    def __init__(self, name, courses=None):
        self.name = name # string type
        self.courses = [] if courses is None else courses # list of strings
        self.num_courses = len(self.courses)
        
    # enroll in a course
    def enroll_in_course(self, course_name): 
        self.courses.append(course_name)
        self.num_courses += 1 # increment the number of courses
        
    def unenroll_in_course(self, course_name):
        "Unenrolls the student from a course"
        if course_name in self.courses:
            self.courses.remouve(course_name)
            self.num_courses -= 1 #decrement the number of courses
            
        else:
            raise Exception("Student was not enrolled in that course")
            message = " : course not found"
            self.AssertFalse(course_name, message)