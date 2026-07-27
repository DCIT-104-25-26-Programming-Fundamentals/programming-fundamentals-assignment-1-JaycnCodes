# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_student(students):
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    try: 
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: Student ID must be an integer.")
        return

    for s in students:
        if s["id"] == student_id:
            print(f"Error: A student with ID {student_id} already exists.")
            return

    try:
        num_scores=int(input("How many scores?"))
        if num_scores <= 0:
            print("Error: Number of scores must be greater than 0.")
            return
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    scores = []
    for i in range(1,num_scores + 1):
        while True:
            try:
                score = float(input(f"Enter score {i}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Error: Score must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid numeric score.")

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')

def display_students(students):
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 65)
    print(f"{'Name':<20} {'ID':<12} {'Scores':<18} {'Average':<8}")
    print("-" * 65)
    for s in students:
        avg_score = sum(s["scores"]) / len(s["scores"]) if s["scores"] else 0.0
        scores_str = ", ".join(
            str(int(sc)) if sc==int(sc) else f"{sc:.2f}" for sc in s["scores"]
        )
        print(f"{s['name']:<20} {s['id']:<12} {scores_str:<18} {avg_score:8.2f}")

def calculate_average(students):
    if not students:
        print("No student records available.")
        return
    try:
        search_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Student ID must be an integer.")
        return

    for s in students:
        if s["id"] == search_id:
            if not s["scores"]:
                print(f"Student {s['name']} has no scores recorded.")
                return
            avg_score = sum(s["scores"]) / len(s["scores"])
            print(f"{s['name']}'s average score: {avg_score:.2f}")
            return

    print(f"Error: No student found with ID {search_id}.")

def display_menu():
    print("   STUDENT RECORD SYSTEM MENU")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

def main():
    students = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
