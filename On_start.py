from login1 import display_options
from Student_1 import display_menu
# program that checks that the username and password are correct 
empty = ''

class Person:
   def __init__(self,x,y):
     self.username = x
     self.password = y

def login():
      Person.username = input("Please enter username: ")
      Person.password = input("Please enter password: ")

      return empty
def do_validation():
    while True:
      if Person.username != "admin" and Person.password != "admin1":
        print("Sorry, wrong information, Please try again")
        login()
      else:
        print("welcome", Person.username)
        break
    return empty
  
print(login())
print(do_validation())

# On start
print("Welcome to the School Management System. Please select an option:")
print(" 1 (Lecturer)  | 2 (Student) | 3 (exit) ")
while True:
    option = input(">>> ")
    if option == "Lecturer" or option == "1":
        print( display_options() )
    elif option == "Student" or option == "2":
        print( display_menu() )
    elif option == "exit" or option == "3":
        break
    else:
        print(option + " is not an option")



