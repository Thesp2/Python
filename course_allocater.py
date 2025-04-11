class Course:
    def __init__(self, code, name, prerequisites, semester):
        self.code = code
        self.name = name
        self.prerequisites = prerequisites
        self.semester = semester

class Student:
    def __init__(self, name, student_id, gender, semester, completed_courses):
        self.name = name
        self.student_id = student_id
        self.gender = gender
        self.semester = semester
        self.completed_courses = set(completed_courses)  # Use a set for faster lookup

    def is_eligible(self, course):
        if course.code in self.completed_courses:
            return False
        if course.semester not in [self.semester, "Elective"]:
            return False
        if course.code == "WOM1000" and self.gender != "female":
            return False
        return set(course.prerequisites).issubset(self.completed_courses)

    def get_eligible_courses(self, courses):
        return [course for course in courses if self.is_eligible(course)]

courses = [
    Course("BCO7006", "Coding for BA", [], 1),
    Course("BCO7000", "Business Analytics", [], 1),
    Course("BCO6008", "Predictive Analytics", ["BCO7006"], 2),
    Course("BCO7007", "Machine Learning", ["BCO7000", "BCO7006"], 2),
    Course("WOM1000", "Women in STEM", [], "Elective")
]

# User Input
name = input("Enter your name: ")
student_id = input("Enter your student ID: ")

gender = input("Enter your gender (male/female): ").strip().lower()
while gender not in {"male", "female"}:
    gender = input("Invalid input!\nEnter 'male' or 'female': ").strip().lower()

semester = input("Enter your semester (1 or 2): ").strip()
while semester not in {"1", "2"}:
    semester = input("Invalid input!\nEnter '1' or '2': ").strip()
semester = int(semester)

valid_courses = {course.code for course in courses}
completed_courses = set()
while True:
    completed_input = input("Enter completed courses (comma-separated, or 'none'): ").strip().lower()
    if completed_input == "none":
        break
    completed_list = set(map(str.strip, completed_input.split(",")))
    if completed_list.issubset(valid_courses):
        completed_courses = completed_list
        break
    print(f"Invalid course entered! Choose from: {', '.join(valid_courses)} or type 'none'.")

# Processing Eligibility
student = Student(name, student_id, gender, semester, completed_courses)
eligible_courses = student.get_eligible_courses(courses)

if not eligible_courses:
    print("\nYou are NOT eligible for any courses this semester.")
else:
    print("\nEligible courses:")
    for course in eligible_courses:
        print(f"{course.code}: {course.name}")
    
    selected_courses = set()
    while True:
        selected_input = set(map(str.strip, input("\nSelect up to 2 courses (comma-separated): ").split(",")))
        if selected_input.issubset({c.code for c in eligible_courses}) and 0 < len(selected_input) <= 2:
            selected_courses = selected_input
            break
        print(f"Invalid selection! Choose up to 2 courses from: {', '.join([c.code for c in eligible_courses])}.")
    
    print("\nEnrollment Successful!")
    for course in selected_courses:
        print(f"| Id {student_id} | Student Name {name} | Code {course} | Semester {semester} |")
