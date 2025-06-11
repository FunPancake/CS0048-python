# Student Grade Tracker

# - A school tracks students' grades for multiple subjects. 
# - Users can add students, add grades for a student, calculate the average grade, and view all students and their grades. 
# - The program should provide a menu for users to select actions (e.g., Add Student, Add Grade, View Grades, Calculate Average). 
# - Use classes for Student and GradeTracker.

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}  # subject -> grade

    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        print(f"Grade added: {subject} = {grade}")

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        if not self.grades:
            return f"{self.name} - No grades available"
        grades_str = ', '.join(f"{subj}: {grade}" for subj, grade in self.grades.items())
        avg = self.calculate_average()
        return f"{self.name} - {grades_str} | Average: {avg:.2f}"


class GradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            print("Student already exists.")
        else:
            self.students[name] = Student(name)
            print("Student added successfully!")

    def add_grade(self, name, subject, grade):
        if name not in self.students:
            print("Student not found.")
        else:
            self.students[name].add_grade(subject, grade)

    def view_grades(self):
        if not self.students:
            print("No students found.")
        else:
            print("\nStudent Grades:")
            for student in self.students.values():
                print(student)

    def calculate_average(self, name):
        if name not in self.students:
            print("Student not found.")
        else:
            avg = self.students[name].calculate_average()
            print(f"{name}'s average grade is: {avg:.2f}")


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
            tracker.add_student(name)
        elif choice == '2':
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            try:
                grade = float(input("Enter grade (0-100): "))
                if 0 <= grade <= 100:
                    tracker.add_grade(name, subject, grade)
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            tracker.view_grades()
        elif choice == '4':
            name = input("Enter student name: ")
            tracker.calculate_average(name)
        elif choice == '5':
            print("Exiting Grade Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()