class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def display_info(self):
        """Display student information."""
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
    
    def calculate_average(self):
        """Calculate and return the average grade."""
        if self.grades:  # Check if the list of grades is not empty
            return sum(self.grades) / len(self.grades)
        else:
            return 0

# Main code to interact with users
students_db = []  # List to store all students

# Function to add a new student to the database
def add_student():
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grades = list(map(int, input("Enter the student's grades separated by commas: ").split(',')))
    
    student = Student(name, age, grades)
    students_db.append(student)
    print(f"\nStudent {name} added to the database.\n")

# Function to display all students' information
def display_all_students():
    if students_db:
        print("\nAll Students in the Database:")
        for student in students_db:
            student.display_info()
            print(f"Average Grade: {student.calculate_average():.2f}\n")
    else:
        print("No students in the database yet.\n")

# Simulating interaction
print("Welcome to the Student Management System")

while True:
    print("\n1. Add a new student")
    print("2. Display all students")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        display_all_students()
    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
