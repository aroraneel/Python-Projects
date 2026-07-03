# Create an empty dictionary to store student names and their marks
student = {}

# Run the program continuously until the user chooses to exit
while True:

    # Display the main menu
    print("\n-----STUDENT MANAGER APP-----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result ")
    print("4. Exit")

    # Take the user's menu choice as input
    choice = input("Enter Your Choice: ")

    # -------------------- Add Student --------------------
    if choice == "1":

        # Ask the user to enter the student's name
        name = input("Enter Student Name: ")

        # Ask the user to enter the student's marks
        # float() is used so decimal marks (e.g., 85.5) can also be entered
        marks = float(input("Enter Marks: "))

        # Store the student's name and marks in the dictionary
        student[name] = marks

        # Display a success message after adding the student
        print(f"{name} Successfully Added!")

    # -------------------- View Students --------------------
    elif choice == "2":

        # Check if the dictionary is empty
        if not student:
            print("NO Student Found!")
        else:
            # Loop through each student and display their name and marks
            for name, marks in student.items():
                print(name, ":", marks)

    # -------------------- Check Result --------------------
    elif choice == "3":

        # Ask the user to enter the student's name
        name = input("Enter Student Name: ")

        # Check if the entered student exists in the dictionary
        if name in student:
            # Get the student's marks
            marks = student[name]

            # Check whether the student has passed or failed
            if marks >= 33:
                print("PASS")
            else:
                print("FAIL")

        # If the student name is not found
        else:
            print("Student Not Found!")

    # -------------------- Exit Program --------------------
    elif choice == "4":
        # Display exit message
        print("Exitting....")
        # Stop the while loop and end the program
        break

    # -------------------- Invalid Choice --------------------
    else:
        # Display an error message if the user enters an invalid menu option
        print("Invalid Choice! Please Try Again.")