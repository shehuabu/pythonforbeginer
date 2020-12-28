# Student Management System
"""
Fields :- ['ID', 'First name','Last name', 'age', 'email', 'phone','Course',Acadamin year']
1. Add New Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Quit
"""
#import os 
import csv
#uid = os.getuid()

# Define global variables
student_fields = ['ID', 'First Name', 'Last Name', 'Age', 'Email', 'Phone', 'Course','Acadamic Year']
student_database = 'students.csv'

def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    print("User ID is:", uid)
    input("Press any key to continue")
    return


def view_students():
    global student_fields
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_student():
    global student_fields
    global student_database

    print("--- Search Student ---")
    ID = input("Enter Student ID. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if ID == row[0]:
                    print("----- Student Found -----")
                    print("ID: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    print("Course: ", row[5])
                    print("Acadamic: ", row[6])
                    break
                
        else:
            print("ID No. not found in our database")
    input("Press any key to continue")


def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    ID = input("Enter Student ID. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Student ID. not found in our database")

    input("Press any key to continue")


def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    ID = input("Enter Student ID. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Student ID. ", ID, "deleted successfully")
    else:
        print("Student ID. not found in our database")

    input("Press any key to continue")

#Display menu options from a list
def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student", "\n2. View Students", "\n3. Search Student", "\n4. Update Student", "\n5. Delete Student", "\n6. Quit" )

    while True:

        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            break
        elif choice != "1" or "2" or "3" or "4" or "5" or "6":
            print("You Enter a wrong choice")
            print("\n")
            print("\n")
            print("\n")
            
        else:
            break

    print("-------------------------------")
    print(" Thank you for using our system")
    print("-------------------------------")

    return ''