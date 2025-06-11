# Student Grade Tracker

# - A school tracks students' grades for multiple subjects. 
# - Users can add students, add grades for a student, calculate the average grade, and view all students and their grades. 
# - The program should provide a menu for users to select actions (e.g., Add Student, Add Grade, View Grades, Calculate Average). 
# - Use classes for Student and GradeTracker.

class Student:
    def __init__(self, name, student_number):
        if not (student_number.isdigit() and len(student_number) == 9):
            raise ValueError("Student number must be exactly 9 digits.")
        self.name = name
        self.student_number = student_number
        self.grades = {}  # subject -> grade

    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        print(f"Grade added: {subject} = {grade}")

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        grades_str = ', '.join(f"{subj}: {grade}" for subj, grade in self.grades.items())
        avg = self.calculate_average()
        return f"{self.name} ({self.student_number}) - {grades_str or 'No grades'} | Average: {avg:.2f}"


class GradeTracker:
    def __init__(self):
        self.students = {}  # student_number -> Student

    def add_student(self, name, student_number):
        if student_number in self.students:
            print("Student number already exists.")
        else:
            try:
                student = Student(name, student_number)
                self.students[student_number] = student
                print("Student added successfully!")
            except ValueError as e:
                print(e)

    def add_grade(self, student_number, subject, grade):
        student = self.students.get(student_number)
        if student:
            student.add_grade(subject, grade)
        else:
            print("Student not found.")

    def view_grades(self):
        if not self.students:
            print("No students found.")
        else:
            print("\nStudent Grades:")
            for student in self.students.values():
                print(student)

    def calculate_average(self, student_number):
        student = self.students.get(student_number)
        if student:
            avg = student.calculate_average()
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
            student_number = input("Enter 9-digit student number: ")
            tracker.add_student(name, student_number)

        elif choice == '2':
            student_number = input("Enter 9-digit student number: ")
            subject = input("Enter subject: ")
            try:
                grade = float(input("Enter grade (0-100): "))
                if 0 <= grade <= 100:
                    tracker.add_grade(student_number, subject, grade)
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid grade input. Must be a number.")

        elif choice == '3':
            tracker.view_grades()

        elif choice == '4':
            student_number = input("Enter 9-digit student number: ")
            tracker.calculate_average(student_number)

        elif choice == '5':
            print("Exiting Grade Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()