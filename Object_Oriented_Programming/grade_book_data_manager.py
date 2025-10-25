# FILE: grade_book_data_manager.py
# CONCEPT: Object-Oriented Programming (OOP) - Dictionary Integration
# DEMONSTRATES: Using a dictionary (self.grades) as internal state, basic data manipulation 
#               (add, remove), and calculating aggregation (average).

class GradeBook:
    def __init__(self):
        self.grades = {}
    
    def add_grades(self, grade, module):
        self.grades[module] = grade
    
    def remove_grade(self, module_name):
        del self.grades[module_name]
        
    def average_grades(self):
        if not self.grades:
            return 0
        
        total_sum = 0
        count = 0
        for i in self.grades.values():
            total_sum = total_sum + i
            count += 1
        return total_sum / count
    
    def __str__(self):
        if self.grades == {}:
            return "The GradeBook is empty"
        else:
            return f"{self.grades}"

def test_grade_book():
    grade_book = GradeBook()
    print(grade_book)
    grade_book.add_grades(7, "math")
    grade_book.add_grades(3, "info")
    print(grade_book)
    average = grade_book.average_grades()
    print(average)
    grade_book.remove_grade("math")
    print(grade_book)
    average = grade_book.average_grades()
    print(average)
    

if __name__ == "__main__":
    test_grade_book()
