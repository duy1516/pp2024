import pickle
import markmanagement
from markmanagement import StudentMarkManager

with open('student.pickle', 'rb') as file:
    student = pickle.load(file)
    
print("List of students:")
    
print(f"Student: {student.student_id}, Name: {student.name}")
