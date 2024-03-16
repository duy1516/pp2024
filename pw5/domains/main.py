import zipper

from markmanagement import  StudentMarkManager
manager = StudentMarkManager()
manager.input_students()
manager.input_courses()
manager.input_marks()
manager.list_courses()
manager.list_students()
manager.show_student_marks()
manager.review()
zipper.zipin()