import zipfile

def zipin():
    with zipfile.ZipFile('student.dat', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
        my_zip.write('course.txt')
        my_zip.write('student.txt')
        my_zip.write('marks.txt')

def zipout():
    with zipfile.ZipFile('student.dat', 'r') as my_zip:
        my_zip.extractall()
       
zipout()