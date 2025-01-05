def input_grades():
    """Function to input grades for subjects."""
    grades = []
    while True:
        try:
            subject = input("Enter the subject name (or 'done' to finish): ")
            if subject.lower() == 'done':
                break
            grade = input(f"Enter grade for {subject}: ")
            grade = float(grade)  # Convert the grade to float
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100.")
            grades.append((subject, grade))
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid grade between 0 and 100.")
    return grades

def calculate_average(grades):
    """Function to calculate the average grade."""
    if not grades:
        return 0
    total_grades = sum(grade for subject, grade in grades)
    return total_grades / len(grades)

def store_grades_in_file(grades):
    """Function to store grades in a file."""
    try:
        with open("grades.txt", "w") as file:
            for subject, grade in grades:
                file.write(f"{subject}: {grade}\n")
        print("Grades have been successfully saved to 'grades.txt'.")
    except IOError as e:
        print(f"Error saving grades to file: {e}")

def main():
    """Main function to run the grade input, calculation, and storage."""
    print("Welcome to the Grade Tracker!")
    
    grades = input_grades()
    
    if grades:
        average_grade = calculate_average(grades)
        print(f"\nThe average grade is: {average_grade:.2f}")
    else:
        print("No grades entered.")
    
    store_grades_in_file(grades)

# Run the program
if __name__ == "__main__":
    main()

