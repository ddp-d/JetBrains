class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = self.name[0] + self.last_name + self.birth_year



student_name = input()
student_surname = input()
student_year = input()

student_one = Student(student_name, student_surname, student_year)

print(student_one.student_id)
