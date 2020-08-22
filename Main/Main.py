class Student:
    def __init__(self, studentId, studentName, studentSurname, studentEmail, studentTel):
        self.studentId = studentId
        self.studentName = studentName
        self.studentSurname = studentSurname
        self.studentEmail = studentEmail
        self.studentTel = studentTel


students = []
students.append(Student("123", "tural", "gulnar", "email@email.com", "2123"))


def FindStudentByStudentId(studentId, students):
    for student in students:
        if student.studentId == studentId:
            return student

def FindStudentByStudentName(studentName, students):
    for student in students:
        if student.studentName == studentName:
            return student

def PressEnterToContinue():
    print("Davam etmək üçün enter-i basın")
    input()

def InsertStudent():
    newStudentId = input("Tələbə kodunu əlavə edin:")
    # newStudentId validation
    while 100 > int(newStudentId) or int(newStudentId) > 999:
        print("Kod 3 reqemli eded olmalidir")
        newStudentId = input("Tələbə kodunu əlavə edin:")

    newStudentName = input("Tələbə adını daxil edin:")
    newStudentSurname = input("Tələbə soyadını daxil edin:")
    newStudentEmail = input("Tələbə emailini daxil edin:")
    # newStudentEmail validation
    while "@" not in newStudentEmail:
        print("Email düzgün deyil!")
        newStudentEmail = input("Tələbə emailini daxil edin:")

    newStudentTel = input("Telefon nömrəsini daxil edin:")
    # newStudentTel validation
    while not newStudentTel.startswith("+994"):
        print("Telefon düzgün deyil!")
        newStudentTel = input("Telefon nömrəsini daxil edin:")

    newStudent = Student(newStudentId, newStudentName, newStudentSurname, newStudentEmail, newStudentTel)
    students.append(newStudent)
    print("Tələbə uğurla əlavə olundu!")
    PressEnterToContinue()

def DeleteStudent():
    studentId = input("Tələbə kodunu daxil edin:")
    deleteStudent = FindStudentByStudentId(studentId, students)
    if deleteStudent is not None:
        students.remove(deleteStudent)
        print("Telebe ugurla silindi")
    else:
        print("Bele telebe tapilmadi")
    PressEnterToContinue()

def EditStudent():
    studentId = input("Tələbə kodunu daxil edin:")
    editStudent = FindStudentByStudentId(studentId,students)
    if editStudent is not None:
        newStudentName = input("Tələbə adını daxil edin:")
        newStudentSurname = input("Tələbə soyadını daxil edin:")
        newStudentEmail = input("Tələbə emailini daxil edin:")
        # newStudentEmail validation
        while "@" not in newStudentEmail:
            print("Email düzgün deyil!")
            newStudentEmail = input("Tələbə emailini daxil edin:")

        newStudentTel = input("Telefon nömrəsini daxil edin:")
        # newStudentTel validation
        while not newStudentTel.startswith("+994"):
            print("Telefon düzgün deyil!")
            newStudentTel = input("Telefon nömrəsini daxil edin:")

        editStudent.studentName = newStudentName
        editStudent.studentSurname = newStudentSurname
        editStudent.studentEmail = newStudentEmail
        editStudent.studentTel = newStudentTel
        students[students.index(editStudent)] = editStudent
        print("Telebe melumatlari ugurla yenilendi")
    else:
        print("Bele telebe tapilmadi")
    PressEnterToContinue()

def ShowStudentByName():
    studentName = input("Tələbə adini daxil edin:")
    showStudent = FindStudentByStudentName(studentName,students)
    if showStudent is not None:
        print("Student Id: " + showStudent.studentId)
        print("Student Name: " + showStudent.studentName)
        print("Student Surname: " + showStudent.studentSurname)
        print("Student Email: " + showStudent.studentEmail)
        print("Student Phone: " + showStudent.studentTel)
        print("-----------------------")
    else:
        print("Bele telebe tapilmadi")
    PressEnterToContinue()

def ShowAllStudents():
    if len(students) > 0:
        for student in students:
            print("Student Id: " + student.studentId)
            print("Student Name: " + student.studentName)
            print("Student Surname: " + student.studentSurname)
            print("Student Email: " + student.studentEmail)
            print("Student Phone: " + student.studentTel)
            print("-----------------------")
    else:
        print("Telebe yoxdur")
    PressEnterToContinue()

while True:
    print("""
    Tələbə əlavə etmək üçün 1
    Tələbə silmək üçün 2
    Tələbə məlumatlarını dəyişdirmək üçün 3
    Tələbə məlumatlarına baxmaq üçün 4
    Bütün tələbələrə baxmaq üçün 5 
    Düyməsinə basın! 
        """)
    userInput = input()

    # New Student
    if userInput == "1":
        InsertStudent()
    elif userInput == "2":
        DeleteStudent()
    elif userInput == "3":
        EditStudent()
    elif userInput == "4":
        ShowStudentByName()
    elif userInput == "5":
        ShowAllStudents()
    else:
        print("Bele bir emeliyyat tapilmadi")


