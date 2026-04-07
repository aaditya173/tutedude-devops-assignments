student_grades = {}

while True:
    print("\nOptions:")
    print("1. Add/Update Student Grade")
    print("2. Print All Student Grades")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        name = input("Enter student's name: ")
        grade = input("Enter student's grade: ")
        student_grades[name] = grade
        print(f"{name}'s grade has been added/updated.")
    
    elif choice == "2":
        if student_grades:
            print("\nAll Student Grades:")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")
        else:
            print("No student grades available.")
    
    elif choice == "3":
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice! Please try again.")