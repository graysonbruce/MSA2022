
def print_main_menu():
    #print the menu
    print("Select option from Menu\n-----------------------")
    print("1. Login")
    print("2. Create User")
    return

def get_user_option():
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
    return user_option

def login_user(u_name, u_pass):
# - validate username and password combination in the users.txt file
    #open the users files
    user_file = open("users.txt", "r")
    user_found = False

    #read the lines from the file
    for line in user_file:
        credentials = line.split(", ")
        #compare username and password for a match
        if u_name == credentials[0] and u_pass == credentials[1].rstrip():
            user_found = True
            break
    return user_found

def create_user(u_name, u_pass):
    pass
def validate_username_or_password(user_credintial, min_length, max_length):
    if (user_credintial >= min_length and user_credintial <=max_length):
        return True
    else:
        print("ERROR: Incorrect username or password length.\n")
        return False 

def main():
    print_main_menu()
    #prompt and get the option the user selected
    user_option = get_user_option()

    if user_option == "1":
        while True:
            #If user chose 1, ask for user name and password and
            user_name = input("Please enter your user name: ")
            user_pass = input("Please enter your password: ")
            user_logged_in = login_user(user_name, user_pass)

            if user_logged_in:
                # - if valid then move on to prompt for student data
                print(f"User {user_name} successfully logged in!\n")
                break
            else:
                # - if not valid combination reprompt the user. 
                print(f"User {user_name} not found!\n")
    
    #If user chose 2, ask for user name and password and
    elif user_option == "2":
        while True:
            #If user chose 2, ask for user name and password and
            user_name = input("Please enter your user name (4 - 12 characters): ")
            user_pass = input("Please enter your password: (6 - 16) characters: ")

            #get username and password length
            user_name_length = len(user_name)
            password_length = len(user_pass)
            
            # - validate username and password length. If valid, write to users.txt file
            # 4 <= user_mame_length >= 12
            if (user_name_length >= 4 and user_name_length <= 12) and (password_length >= 6 and password_length <= 16):
                #write user and pass to the file
                user_file = open("users.txt", "a")
                user_file.write(f"{user_name}, {user_pass}\n")
                user_file.close()
                break
            else:
                print("ERROR: Incorrect username or password length.\n")

    print("Ask user for student data")
    #Create 3 empty list for student name, scores, letter grades
    student_names = []
    student_scores = []
    student_letter_grades = []

    #Ask user how many students to enter data for
    number_of_students = int(input("Enter number of students to enter grades for: "))

    for counter in range(number_of_students):
        #prompt user to enter student name and number score
        student_name = input("Enter student name: ")
        student_score = float(input("Enter student score: "))
        
        #store data in the lists
        student_names.append(student_name)
        student_scores.append(student_score)
        
        #convert the current number score to a letter grade and store in the letter grade list
        #use and If...elif...else statement
        if student_score >= 90:
            student_letter_grades.append("A")
        elif student_score >= 80:
            student_letter_grades.append("B")
        elif student_score >= 70:
            student_letter_grades.append("C")
        elif student_score >= 60:
            student_letter_grades.append("D")
        else:
            student_letter_grades.append("F")

    #Print student data(name, score, grade)
    for index in range(len(student_names)):
        print(f"{student_names[index]} : {student_scores[index]} : {student_letter_grades[index]}")

    #Calculate and print class average
    avg = sum(student_scores) / len(student_scores)
    print(f"Class Average: {avg}")

main()