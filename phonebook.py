# importing the modules
import sys

# this function will be the first to run as soon as the main function executes
def intial_phonebook():
    rows, cols = int(input("please enter initial amount of contacts: ")), 5

    # We are collecting the initial number of contacts from the user wants to have in the
    #phonebook aldready. user must press one if he doesn't want to nter any.
    phonebook = []
    print(phonebook)
    for i in range(rows):
        print("\nEnter contact %d in the following order (ONLY) :" % (i + 1))
        print("NOTE: * indicates mandatory fields")

print(".................................................................................................................................")
temp = []
cols = 5  # Define cols before using it
for j in range(cols):
    # we have taken conditions for the j only for personalized fields
    # such as name, number, e-mail, id, dob, category ect
    if j == 0:
        temp.append(str(input("Enter Name*: ")))
        # we need to make sure that the name field is empty
        # name & number are mandatory fields.
        # So a condition to check is below
        if temp[j] == '' or temp[j] == ' ':
            sys.exit("Name field cannot be empty. Exiting the program...")
            # this process will exit if the name field is empty
temp.append(str(input("Enter Number* (with country code): ")))
if temp[j] == '' or temp[j] == ' ': 
    sys.exit("Number field cannot be empty. Exiting the program...")    
if j == 2:
    temp.append(str(input("Enter E-mail: ")))
    # even i this field is empty none will take the blank space
    if temp[j] == '' or temp[j] == ' ':
        temp[j] = 'None'
if j == 3:
    temp.append(str(input("Enter DOB (DD/MM/YYYY): ")))
    if temp[j] == '' or temp[j] == ' ':
        # whatever the user enters in the dob field it will not make a difference
        # Only while searching user has to enter the exact same format
        # he entered while adding the contact
        if temp[j] == '' or temp[j] == ' ':
            temp[j] = 'None'    
if j == 4:
    temp.append(str(input("Enter Category (Family/Friends/Work/Others): ")))
    if temp[j] == '' or temp[j] == ' ':
        temp[j] = 'None'
    phonebook.append(temp)
    print("phone_book")
    return phonebook        

        pass