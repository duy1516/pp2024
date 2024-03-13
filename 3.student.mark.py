import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

class StudentMarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        num_students = int(input("Enter number of students in the class: "))
        for i in range(num_students):
            student_id = input(f"Enter student ID for student {i+1}: ")
            name = input(f"Enter student name for student {i+1}: ")
            dob = input(f"Enter student date of birth (DOB) for student {i+1}: ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for i in range(num_courses):
            course_id = input(f"Enter course ID for course {i+1}: ")
            name = input(f"Enter course name for course {i+1}: ")
            credit = int(input(f"Enter credit for course {i+1}: "))
            course = Course(course_id, name, credit)
            self.courses.append(course)

    def input_marks(self):
        print("Available courses:")
        for idx, course in enumerate(self.courses):
            print(f"{idx + 1}. {course.name}")
        selected_course = int(input("Select a course by entering its number: ")) - 1

        course_id = self.courses[selected_course].course_id
        self.marks[course_id] = {}

        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} in {self.courses[selected_course].name} (ID: {student.student_id}): "))
            mark = math.floor(mark * 10) / 10  # Round down to 1-digit decimal
            self.marks[course_id][student.student_id] = mark

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Name: {course.name}, Credit: {course.credit}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"Student ID: {student.student_id}, Name: {student.name}")

    def calculate_gpa(self, student_id):
        total_credit = 0
        weighted_sum = 0
        for course in self.courses:
            course_id = course.course_id
            if course_id in self.marks and student_id in self.marks[course_id]:
                mark = self.marks[course_id][student_id]
                weighted_sum += mark * course.credit
                total_credit += course.credit
        if total_credit == 0:
            return 0
        return weighted_sum / total_credit

    def sort_students_by_gpa(self):
        sorted_students = sorted(self.students, key=lambda student: self.calculate_gpa(student.student_id), reverse=True)
        return sorted_students

    def show_student_marks(self):
        print("Available courses:")
        for idx, course in enumerate(self.courses):
            print(f"{idx + 1}. {course.name}")
        selected_course = int(input("Select a course by entering its number: ")) - 1

        course_id = self.courses[selected_course].course_id

        if course_id not in self.marks or not self.marks[course_id]:
            print("Marks for this course have not been input yet.")
            self.input_marks()
        else:
            print(f"Student marks for {self.courses[selected_course].name}:")
            for student_id, mark in self.marks[course_id].items():
                student_name = [student.name for student in self.students if student.student_id == student_id][0]
                print(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark}")

# Test the classes
manager = StudentMarkManager()
manager.input_students()
manager.input_courses()
manager.input_marks()
manager.list_courses()
manager.list_students()
manager.show_student_marks()

# Calculate average GPA for a given student
student_id = input("Enter student ID to calculate average GPA: ")
average_gpa = manager.calculate_gpa(student_id)
print(f"Average GPA for student with ID {student_id}: {average_gpa}")

# Sort student list by GPA descending
sorted_students = manager.sort_students_by_gpa()
print("Students sorted by GPA descending:")
for student in sorted_students:
    print(f"Student ID: {student.student_id}, Name: {student.name}, GPA: {manager.calculate_gpa(student.student_id)}")
