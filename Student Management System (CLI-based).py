# Student Management System

class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, age, id, gpa):
        if id in self.students:
            print("A student with this ID already exists.")
        else:
            self.students[id] = {
                "name": name,
                "age": age,
                "gpa": gpa
            }
            print("The student has been successfully added to the database.")

    def view_all_students(self):
        if not self.students:
            print("No students in the database.")
        else:
            print("\n--- All Students ---")
            for id, info in self.students.items():
                print(f"ID: {id} | Name: {info['name']} | Age: {info['age']} | GPA: {info['gpa']}")

    def search_student(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print("\n--- Student Found ---")
            print(f"ID: {student_id} | Name: {student['name']} | Age: {student['age']} | GPA: {student['gpa']}")
        else:
            print("\nStudent not found")

    def update_student(self, student_id):
        if student_id not in self.students:
            print("The student is not found in our database.")
            return

        print("\n--- Current Info ---")
        student = self.students[student_id]
        print(f"Name: {student['name']} | Age: {student['age']} | GPA: {student['gpa']}")

        print("\nEnter new values (leave blank to keep current):")

        name = input("New name: ").strip()
        age_input = input("New age: ").strip()
        gpa_input = input("New GPA: ").strip()

        if name:
            student['name'] = name
        if age_input:
            try:
                student['age'] = int(age_input)
            except ValueError:
                print("Invalid age input. Keeping previous age.")
        if gpa_input:
            try:
                student['gpa'] = float(gpa_input)
            except ValueError:
                print("Invalid GPA input. Keeping previous GPA.")

        print("Student information updated successfully.")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("The student is not found in our database.")
        else:
            del self.students[student_id]
            print("The student was removed.")


def main(school):
    print("-------------------------------")
    print("- Student Management System   -")
    print("-------------------------------")

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Enter student name: ")
            try:
                age = int(input("Enter age: "))
                id = int(input("Enter ID: "))
                gpa = float(input("Enter GPA: "))
            except ValueError:
                print("Invalid input. Please enter numbers for age, ID, and GPA.")
                continue
            school.add_student(name, age, id, gpa)

        elif choice == 2:
            school.view_all_students()

        elif choice == 3:
            try:
                student_id = int(input("Enter the ID of the student: "))
                school.search_student(student_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == 4:
            try:
                student_id = int(input("Enter the ID of the student: "))
                school.update_student(student_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == 5:
            try:
                student_id = int(input("Enter the ID of the student: "))
                school.delete_student(student_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == 6:
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

my_school = School()
main(my_school)
