from student import Student
from course import Course

class StudentMarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        num_students = int(input("Enter number of students in the class: "))
        for i in range(num_students):
            student_id = input(f"Enter student student_id for student {i+1}: ")
            name = input(f"Enter student name for student {i+1}: ")
            dob = input(f"Enter student {i+1} date of birth: ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for i in range(num_courses):
            course_student_id = input(f"Enter course student_id for course {i+1}: ")
            name = input(f"Enter course name for course {i+1}: ")
            course = Course(course_student_id, name)
            self.courses.append(course)

    def input_marks(self):
        print("Available courses:")
        for student_idx, course in enumerate(self.courses):
            print(f"{student_idx + 1}. {course.name}")
        selected_course = int(input("Select a course by entering its number: ")) - 1

        course_student_id = self.courses[selected_course].course_student_id
        self.marks[course_student_id] = {}

        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} in {self.courses[selected_course].name} (student_id: {student.student_id}): "))
            self.marks[course_student_id][student.student_id] = mark

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"Course student_id: {course.course_student_id}, Name: {course.name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"Student student_id: {student.student_id}, Name: {student.name}")

    def show_student_marks(self):
        print("Available courses:")
        for student_idx, course in enumerate(self.courses):
            print(f"{student_idx + 1}. {course.name}")
        selected_course = int(input("Select a course by entering its number: ")) - 1

        course_student_id = self.courses[selected_course].course_student_id

        if course_student_id not in self.marks or not self.marks[course_student_id]:
            print("Marks for this course have not been input yet.")
            self.input_marks()
        else:
            print(f"Student marks for {self.courses[selected_course].name}:")
            for student_id, mark in self.marks[course_student_id].items():
                student_name = [student.name for student in self.students if student.student_id == student_id][0]
                print(f"Student student_id: {student_id}, Name: {student_name}, Mark: {mark}")