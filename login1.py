  # lecturer Management System
"""
Fields :- ['ID', 'First Name', 'Last Name','Email', 'Phone', 'Course']
1. Add New lecturer
2. View lecturer
3. Search lecturer
4. Update lecturer
5. Delete lecturer
6. Quit
"""

import csv
# Define global variables
lecturer_fields = ['ID', 'First Name', 'Last Name','Email', 'Phone', 'Course']
lecturer_database = 'lecturer.csv'

def add_lecturer():
    print("-------------------------")
    print("Add lecturer Information")
    print("-------------------------")
    global lecturer_fields
    global lecturer_database

    lecturer_data = []
    for field in lecturer_fields:
        value = input("Enter " + field + ": ")
        lecturer_data.append(value)

    with open(lecturer_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([lecturer_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def view_lecturer():
    global lecturer_fields
    global lecturer_database

    print("--- lecturer Records ---")

    with open(lecturer_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in lecturer_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_lecturer():
    global lecturer_fields
    global lecturer_database

    print("--- Search lecturer ---")
    ID = input("Enter lecturer ID. to search: ")
    with open(lecturer_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if ID == row[0]:
                    print("----- lecturer Found -----")
                    print("ID: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    print("Course: ", row[5])
                    break
        else:
            print("ID No. not found in our database")
    input("Press any key to continue")


def update_lecturer():
    global lecturer_fields
    global lecturer_database

    print("--- Update lecturer ---")
    ID = input("Enter lecturer ID. to update: ")
    index_lecturer = None
    updated_data = []
    with open(lecturer_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID == row[0]:
                    index_lecturer = counter
                    print("lecturer Found: at index ",index_lecturer)
                    lecturer_data = []
                    for field in lecturer_fields:
                        value = input("Enter " + field + ": ")
                        lecturer_data.append(value)
                    updated_data.append(lecturer_data)
                else:
                    updated_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_lecturer is not None:
        with open(lecturer_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("lecturer ID. not found in our database")

    input("Press any key to continue")


def delete_lecturer():
    global lecturer_fields
    global lecturer_database

    print("--- Delete lecturer ---")
    ID = input("Enter lecturer ID. to delete: ")
    lecturer_found = False
    updated_data = []
    with open(lecturer_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    lecturer_found = True

    if lecturer_found is True:
        with open(lecturer_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("lecturer ID. ", ID, "deleted successfully")
    else:
        print("lecturer ID. not found in our database")

    input("Press any key to continue")

    
#Display menu options from a list
def display_options():
    print("--------------------------------------")
    print(" Welcome to Lecturer Management System")
    print("---------------------------------------")
    print("1. Add New Lecturer", "\n2. View Lecturer", "\n3. Search Lecturer", "\n4. Update Lecturer", "\n5. Delete Lecturer", "\n6. Quit" )

    while True:

        choice = input("Enter your choice: ")
        if choice == '1':
            add_lecturer()
        elif choice == '2':
            view_lecturer()
        elif choice == '3':
            search_lecturer()
        elif choice == '4':
            update_lecturer()
        elif choice == '5':
            delete_lecturer()
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









