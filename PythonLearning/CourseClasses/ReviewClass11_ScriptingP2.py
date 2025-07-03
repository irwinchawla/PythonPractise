#Correct way to exit applications and using nested conditions for programs
import sys

def get_number():
    try:
        return int(input("Enter Number: "))
    except ValueError:
        return None

a = get_number()

if a is not None:
    print('Your Number is', a)
else:
    print('You have entered a wrong value.')
    choice = input('Press 1 to try again, Press 2 to exit: ')
    
    if choice == '1':
        a = get_number()
        if a is not None:
            print('Your Number is', a)
        else:
            print('Wrong input again. Exiting application.')
            sys.exit()
    else:
        print('Exiting application.')
        sys.exit()
