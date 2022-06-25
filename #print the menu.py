#print the menu


print("Select option from Menu\n-----------------------")
print("1. Login")
print("2. Create User")

#prompt and get the option the user selected
while True:
    user_option = input("Would you like to (1) login or (2)create account? ")
    #Ensure the user entered a valid option (1 or 2)
    if user_option != "1" and user_option != "2":
        # -if not, prompt user again
        print("\nERROR: Enter a 1 or 2")
        continue
    else:
        print("YaY! Good input")
        break     


if user_option == "1":
    while True:
        #If user chose 1, ask for user name and password and
        user_name = input("Please enter your user name: ")
        user_pass = input("Please enter your password: ")
        # - validate username and password combination in the users.txt file
        #open the users files
        user_file = open("users.txt", "r")
        user_found = False

        #read the lines from the file
        for line in user_file:
            credentials = line.split(", ")
             #compare username and password for a match
            if user_name == credentials[0] and user_pass == credentials[1].rstrip():
                user_found = True
                break

        if user_found:
            # - if valid then move on to prompt for student data
            print(f"User {user_name} successfully logged in!\n")
            break
        else:
            # - if not valid combination reprompt the user. 
            print(f"User {user_name} not found!\n")
        
#If user chose 2, ask for user name and password and
elif user_option == "2":
        run_again = True
        while(run_again):
            #If user chose 2, ask for user name and password and
            user_name = input("Please enter your user name (4 - 12 characters): ")
            user_pass = input("Please enter your password: (6 - 16 characters): ")
            #get username and password length
            username_length = len(user_name)
            password_length = len(user_pass)

            # - validate username and password length. If valid, write to users.txt file
            if(username_length >=4 and username_length <=12 and password_length >=6 and password_length <=16):
                user_file = open("users.txt", "a")
                user_file.write(user_name)
                user_file.write(", ")
                user_file.write(user_pass)
                user_file.write("\n")
                user_file.close()
                print("\nAccount successfully created")
                run_again = False 
            else:
                print("ERROR: Incorrect password length and/or username length")
                continue
print("Ask user for student data")
#create 3 empty lists for student name, scores, and letter grade
list_of_student_names = []
list_of_student_scores = []
list_of_letter_grades = []
#Ask user how many students to enter data for
number_of_students = input("How many student names there are")
#prompt user to enter student name and number score
#store data somewhere
#convert the number score to a letter grade 

#Print student data(name, score, grade)
#Calculate and print class average