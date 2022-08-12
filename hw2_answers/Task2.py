class Student():

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

class CFGStudent(Student):
    def __init__(self,
                 name,
                 age,
                 id):
        super(CFGStudent, self).__init__(name, age, id)

    def add_subject(self, subject_and_grade):
        self.subjects.update(subject_and_grade)

    def remove_subject(self, subjects):
        self.subjects.pop(subjects)

    def view_subject(self):
        for subject, grade in self.subjects.items():
                print(f"{subject} ... {grade}")

    def view_grade(self):
        total_grade = sum(self.subjects.values())
        return total_grade

#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

new_student = CFGStudent('Emma', 32, 1)
alum_student = CFGStudent('JJ', 27, 2)

print(new_student.name)
new_student.add_subject({'SQL': 95})
new_student.add_subject({'Python': 93})
new_student.add_subject({'Cloud': 90})
new_student.add_subject({'Agile': 88})
new_student.remove_subject('SQL')
new_student.view_subject()
print(f'Total grade: {new_student.view_grade()}')
print('\n')
print(alum_student.name)
alum_student.add_subject({'Mobile': 88})
alum_student.add_subject({'OOP': 78})
alum_student.view_subject()
print(f'Total grade: {alum_student.view_grade()}')

