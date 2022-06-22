import math

# function 
def get_float_value(prompt):
    run_again = True
    while (run_again):
        try:
            user_input = float(input(prompt))
            if(user_input <= 0):
                print("ERROR: Value must be greater than 0.\n")
                continue
        except:
            print("ERROR: Input must be a number.\n")
        else:
            run_again = False
    
    return user_input 

do_again = True 
while do_again: 
    # Float values/Variables 
    radius_of_cylinder = get_float_value("What is the radius of the cylinder: ")
    height_of_cylinder = get_float_value("What is the height of the cylinder: ") 

    # Print the value of pi
    print (math.pi)

    # Calculations 
    Volume_of_cylinder = math.pi * radius_of_cylinder * 2 * height_of_cylinder 
    print(" Volume of a cylinder: " , Volume_of_cylinder )

    rerun = input("Would you like to perform another calculation (y/n)? ")
    if rerun == "n":
        do_again = False 
