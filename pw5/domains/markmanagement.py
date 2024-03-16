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
            student_id = input(f"Enter student id for student {i+1}: ")
            name = input(f"Enter student name for student {i+1}: ")
            dob = input(f"Enter student {i+1} date of birth: ")
            student = Student(student_id, name, dob)
            self.students.append(student)
        with open('student.txt', 'w') as w:
            for student in self.students:
                w.write(f"Student ID: {student.student_id}, Name: {student.name}, DOB: {student.dob}\n")

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for i in range(num_courses):
            course_id = input(f"Enter course id for course {i+1}: ")
            name = input(f"Enter course name for course {i+1}: ")
            course = Course(course_id, name)
            self.courses.append(course)
        with open('course.txt', 'w') as w:
            for course in self.courses:
                w.write(f"Course ID: {course.course_id}, Course name: {course.name},\n")

    def input_marks(self):
        print("Available courses:")
        for student_idx, course in enumerate(self.courses):
            print(f"{student_idx + 1}. {course.name}")
        selected_course = int(input("Select a course by entering its number: ")) - 1

        course_id = self.courses[selected_course].course_id
        self.marks[course_id] = {}

        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} in {self.courses[selected_course].name} (student_id: {student.student_id}): "))
            self.marks[course_id][student.student_id] = mark
        with open('marks.txt', 'a') as f:
            f.write(f"Course: {self.courses[selected_course].name}\n")
            for student_id, mark in self.marks[course_id].items():
                student_name = next(student.name for student in self.students if student.student_id == student_id)
                f.write(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark}\n")

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"Course student_id: {course.course_id}, Name: {course.name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"Student student_id: {student.student_id}, Name: {student.name}")

    def show_student_marks(self):
        print("Available courses:")
        for student_idx, course in enumerate(self.courses):
            print(f"{student_idx + 1}. {course.name}")
        selected_course = int(input("Select a course by entering its number: ")) - 1

        course_id = self.courses[selected_course].course_id

        if course_id not in self.marks or not self.marks[course_id]:
            print("Marks for this course have not been input yet.")
            self.input_marks()
        else:
            print(f"Student marks for {self.courses[selected_course].name}:")
            for student_id, mark in self.marks[course_id].items():
                student_name = [student.name for student in self.students if student.student_id == student_id][0]
                print(f"Student student_id: {student_id}, Name: {student_name}, Mark: {mark}")
                
                
    def review(self):
        print("Do you want to view the marks in another course? ")
        while True:
            choice = input("Type (y/n): ")
            if choice == 'y':
                StudentMarkManager.show_student_marks(self)
            elif choice == 'n':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please type 'y' or 'n'.")