from student import Student
import unittest

class UnenrollInTestCase(unittest.TestCase):
    def test_01_incremented_correctly(self):
        student1 = Student('Katherine', ['DS 5100'])
        student1.enroll_in_course("CS 5050")
        student1.enroll_in_course("CS 5777")
        print(student1.courses)
        print(student1.num_courses)
        
        #test
        expected = 3
        #unittest.TestCase brings in the assertEqual() method
        self.assertEqual(student1.num_courses, expected)
        
    def test_02_decrement_correctly(self):
        student1 = Student('Katherine', ['DS 5100'])
        course = 'CS 5050'
        student1.unenroll_in_course(course)
        student1.unenroll_in_course(course)
        self.assertFalse(course in student1.courses) #course should not be in list
        
    def test_03_is_course_not_added(self):
        student1 = Student('Katherine', ['DS 5100']) #initialize
        expected = len
        
        #test
        expected = 0
        self.assertEqual(student2.num_courses, expected)
        
if __name__ == '__main__':
    unittest.main(verbosity = 2)
    
    
        