# FILE: student_management_system.py
# CONCEPT: Object-Oriented Programming (OOP) - Data Validation and Inheritance
# DEMONSTRATES: Using conditional logic in __init__ and property setters for data integrity,
#               and inheritance (PlacementStudent) to model specialized student types.

class Student:
    
    courses = {"Computer Science", "Software Engineering", "Networks and Security", "Data Science", "Cybersecurity", "Computing"}
    
    def __init__(self, up_number, course, year):
        # Validation logic in __init__
        if up_number.startswith("up"):
            self._up_number = up_number
        else:
            self._up_number = None
            
        if course in self.courses:
            self._course = course
        else:
            self._course = "Unknown"
            
        if 1 <= year <= 4:
            self._year = year
        else:
            self._year = 1
        
    @property
    def course(self):
        return self._course
    
    @course.setter
    def course(self, new_course):
        if new_course in self.courses:
            self._course = new_course
            
    @property
    def up_number(self):
        return self._up_number
    
    @property
    def year(self):
        return self._year
    
    def progress(self, new_year):
        # Allows progression only to a valid, future year
        if 1 <= new_year <= 4 and new_year > self._year:
            self._year = new_year
        
    def __str__(self):
        return f"Student {self._up_number} studying {self._course} in year {self._year}"
    
class PlacementStudent(Student):
    
    def __init__(self, up_number, course, year, company):
        # Placement students typically must be in Year 3 to start placement
        if year == 3:
            super().__init__(up_number, course, year)
            self.company = company
        else:
            super().__init__(up_number, course, year)
            self.company = "N/A (Invalid Year for Placement Init)"
            
    def __str__(self):
        return f"Placement student {self._up_number} working at {self.company} (Year {self._year})"
        
    
def test_students():
    student = Student("up2283959", "Computer Science", 4)
    student2 = Student("up283959", "Data Science", 2)
    print(student)
    print(student2)
    student2.progress(3)
    print(student2)
    
    # Test valid placement student init
    student3 = PlacementStudent("up22432159", "Computing", 3, "Google")
    print(student3)
    
    # Test invalid placement student init (Year 4)
    student4 = PlacementStudent("up1234567", "Computing", 4, "Amazon")
    print(student4)
    
    
if __name__ == "__main__":
    test_students()
