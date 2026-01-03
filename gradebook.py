class Student:
    #initialization 
    def __init__(self, name):
        self.__name = name
        self.__grades = []

    #getter method for student grades
    def get_grades(self):
        return self.__grades

    #getter method for student name
    def get_name(self):
        return self.__name

    def add_grade(self, grade):
        #grade is considered valid (added to list) if between bounds
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("Invalid Grade! Must be between 0 and 100.")

    def average(self):
        #if there is nothing in list, average = 0
        if len(self.__grades) == 0:
            return 0
        total = 0
        for item in self.__grades:
            total += item
        #cast the average to int to match the examples in directions
        return int(total / len(self.__grades))


    def letter_grade(self):
        student_average = self.average()

        #if statement to assign letter grades based on average
        if student_average >= 90:
            return "A"
        elif 80 <= student_average < 90:
            return "B"
        elif 70 <= student_average < 80:
            return "C"
        elif 60 <= student_average < 70:
            return "D"
        else:
            return "F"

    def gpa(self):
        student_letter = self.letter_grade()
        #dictionary with letter grades as keys and GPA as values
        grade_equivalence = {
            "A": 4.0,
            "B": 3.0,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0
        }

        #will return corresponding GPA
        return grade_equivalence[student_letter]

    #format string
    def __str__(self):
        return self.__name + " | Grades: " + str(self.__grades) + " | Avg: " + str(self.average()) + " | Letter Grade: " + self.letter_grade() + " | GPA: " + str(self.gpa())

#add a new student without duplicating if student is already in system
def add_student(gradebook):
    name = input("Enter student name: ")
    if name in gradebook:
        print("Student already exists.")
    else:
        new_student = Student(name)
        gradebook[name] = new_student
        print("Student added.")

#add a grade into a student's grade list
def add_grade_to_student(gradebook):
    name = input("Enter student name: ")
    if name not in gradebook:
        print("Student not found.")
        return
    grade_string = input("Enter grade (0-100): ")
    grade = float(grade_string)

    student = gradebook[name]
    student.add_grade(grade)
    print("Grade added.")

#shows info for all students in gradebook
def display_all_students(gradebook):
    if len(gradebook) == 0:
        print("No students yet.")
        return
    for name in gradebook:
        student = gradebook[name]
        print(student)

#uses student average to calculate the class average
def class_average(gradebook):
    #class average is 0 if there are no students
    if len(gradebook) == 0:
        print("No students yet.")
        return
    
    sum_average = 0
    num_students = 0

#add up each student average, divide by number of students
    for name in gradebook:
        student = gradebook[name]
        sum_average += student.average()
        num_students += 1
    
    if num_students == 0:
       average = 0
    else:
       #using / operator returns float, cast to int
       average = int(sum_average/num_students)
    
    print("Class average: " + str(average))


#remove info if student is deleted
def delete_student(gradebook):
    name = input("Enter student name to delete: ")
    if name in gradebook:
        del gradebook[name]
        print("Student deleted.")
    else:
        print("Student not found.")

#opens student_info.txt , converts each student to string, writes in info
def save_to_file(gradebook, filename="student_info.txt"):
    file = open(filename, "w")

    for name in gradebook:
        student = gradebook[name]
        line = str(student) 
        file.write(line + "\n")

    file.close()

#open gradebook.txt, split lines into name and grades and creates student object
def load_from_file(filename="gradebook.txt"):
    gradebook = {}

    file = open(filename, "r")

    for line in file:
        line = line.strip()

        if line != "":
            parts = line.split(":")
            name = parts[0].strip()
            grades_part = parts[1]

            student = Student(name)

            #each grade string is casted to float
            grades_strings = grades_part.split(",")
            for item in grades_strings:
                item = item.strip()
                if item != "":
                    grade = float(item)
                    student.add_grade(grade)

            #student is stored in the gradebook 
            gradebook[name] = student

    file.close()
    return gradebook


