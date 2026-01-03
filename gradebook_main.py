import gradebook as fp

#multi line string for menu text
menu_text = '''
=== MENU ===
1. Add Student
2. Add Grade to Student
3. Display All Students
4. Class Average
5. Delete Student
6. Save and Exit
Choose (1-6): '''

def main():
    print("Welcome to the Student Gradebook Manager!")

    gradebook = fp.load_from_file()

    user_choice = input(menu_text)

    #call methods based on number selected by user
    while user_choice != "6":
        if user_choice == "1":
            fp.add_student(gradebook)
        elif user_choice == "2":
            fp.add_grade_to_student(gradebook)
        elif user_choice == "3":
            fp.display_all_students(gradebook)
        elif user_choice == "4":
            fp.class_average(gradebook)
        elif user_choice == "5":
            fp.delete_student(gradebook)
        else:
            print("Invalid option.")

        user_choice = input(menu_text)

    fp.save_to_file(gradebook)

#call to main function
if __name__ == "__main__":
    main()