# Student Grade Tracker

# - A school tracks students' grades for multiple subjects. 
# - Users can add students, add grades for a student, calculate the average grade, and view all students and their grades. 
# - The program should provide a menu for users to select actions (e.g., Add Student, Add Grade, View Grades, Calculate Average). 
# - Use classes for Student and GradeTracker.

class Student:
    def __init__(self, name, studentnumber):
        self.name = name
        self.studentnumber = studentnumber
        self.grade = {}

    def addgrade(self, subject, grade):
        self.grade[subject] = grade
        print(f"Grade added: {subject} = {grade}")  # Fixed string formatting

    def calcgrade(self):
        if not self.grade:
            return 0
        return sum(self.grade.values()) / len(self.grade)

    def __str__(self):
        grades_str = ", ".join(f"{subj}: {grade}" for subj, grade in self.grade.items())
        avg = self.calcgrade()
        return f"{self.name} {self.studentnumber} - {grades_str or 'no Grades'} | Average: {avg:.2f}"


class GradeTracker:
    def __init__(self):
        self.students = {}

    def addstudent(self, name, studentnumber):  # Changed param order
        if studentnumber in self.students:
            print("Student number already exists.")
        else:
            student = Student(name, studentnumber)
            self.students[studentnumber] = student
            print("Student added successfully!")

    def addgrade(self, studentnumber, subject, grade):
        student = self.students.get(studentnumber)
        if student:
            student.addgrade(subject, grade)
        else:
            print("Student not found.")

    def viewgrades(self):
        if not self.students:
            print("No students found.")
        else:
            print("\nStudent Grades:")
            for student in self.students.values():
                print(student)

    def calcgrade(self, studentnumber):
        student = self.students.get(studentnumber)
        if student:
            avg = student.calcgrade()
            print(f"{student.name}'s average grade is: {avg:.2f}")
        else:
            print("Student not found.")


def main():
    tracker = GradeTracker()

    while True:
        print("\nGrade Tracker Menu:")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View All Students & Grades")
        print("4. Calculate Student's Average")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student name: ")
            studentnumber = input("Enter student number: ")
            tracker.addstudent(name, studentnumber)

        elif choice == '2':
            studentnumber = input("Enter student number: ")
            subject = input("Enter subject: ")
            try:
                grade = float(input("Enter grade (0-100): "))
                if 0 <= grade <= 100:
                    tracker.addgrade(studentnumber, subject, grade)
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid grade input. Must be a number.")

        elif choice == '3':
            tracker.viewgrades()

        elif choice == '4':
            studentnumber = input("Enter student number: ")
            tracker.calcgrade(studentnumber)

        elif choice == '5':
            print("Exiting Grade Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
