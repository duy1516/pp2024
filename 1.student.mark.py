# Initialize empty lists and dictionaries to store data
students = []
courses = []
marks = {}  # Dictionary to store student marks for each course

# Function to input student information
def input_students():
    num_students = int(input("Enter number of students in the class: "))
    for i in range(num_students):
        student_id = input(f"Enter student ID for student {i+1}: ")
        student_name = input(f"Enter student {i+1} name: ")
        DoB = input(f"Enter student {i+1} date of birth: ")
        student_info = (student_id, student_name, DoB)
        students.append(student_info)   

# Function to list all students
def list_students():
    print("List of students:")
    for student in students:
        print(f"Student ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

# Function to input course information2
def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
        course_id = input(f"Enter the ID of course number {i+1}: ")
        name = input("Enter course name: ")
        course_info = (course_id, name)
        courses.append(course_info)

# Function to list all courses
def list_courses():
    print("List of courses:")
    for course in courses:
        print(f"Course ID: {course[0]}, Name: {course[1]}")
        
# Function to input marks for a selected course
def input_marks():
    print("Choose the course to input students' marks")
    for idx, course in enumerate(courses):
        print(f"{idx + 1}. {course[1]}")
    selected_course = int(input("Select a course: ")) - 1

    course_id = courses[selected_course][0]
    marks[course_id] = {}

    for student in students:
        mark = float(input(f"Enter mark for the student with ID {student[0]} in {courses[selected_course][1]}: "))
        marks[course_id][student[0]] = mark



# Function to show student marks for a given course
def show_student_marks():
    print("Choose the course to view students' marks")
    for idx, course in enumerate(courses):
        print(f"{idx + 1}. {course[1]}")
    selected_course = int(input("Select a course: ")) - 1

    course_id = courses[selected_course][0]

    if course_id not in marks or not marks[course_id]:
        print("Marks for this course have not been input yet.")
        input_marks()  
        show_student_marks()
    else:
        print(f"Student marks for {courses[selected_course][1]}:")
        for student_id, mark in marks[course_id].items():
            student_name = [student[1] for student in students if student[0] == student_id][0]
            print(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark}")

# Test the functions
input_students()
list_students()
input_courses()
list_courses()
input_marks()
show_student_marks()
