# Student Gradebook Manager

# Overview
This project is a command-line Student Gradebook Manager developed as a final project for an Introduction to Programming course. The program allows users to manage a class gradebook by adding students, recording grades, displaying student information, computing class averages, and saving data to a file.

The application uses a menu-driven interface and demonstrates core programming concepts such as functions, loops, conditional logic, file input/output, and modular program design.

---

# Program Features
The Gradebook Manager allows the user to:
1. Add a new student to the gradebook
2. Add grades to an existing student
3. Display all students and their grades
4. Calculate and display the class average
5. Delete a student from the gradebook
6. Save the gradebook data and exit the program

---

## How the Program Works
- When the program starts, it loads previously saved gradebook data from a file.
- The user interacts with the program through a numbered menu.
- Each menu option calls a specific function from the `gradebook` module.
- The program continues running until the user chooses to save and exit.
- Upon exit, all gradebook data is written back to a file for future use.

---

- `gradebook_main.py` – Handles user interaction and menu logic  
- `gradebook.py` – Contains functions for managing students and grades  
- `gradebook.txt` – Stores saved gradebook data 
