"""
Assignment 3.
"""
##Place your import statements below this line
from datetime import datetime

def main():
    """
    Enter your code below. Ensure your code is within the body of the main() function.
    i.e. it is tabbed-in at least once.
    """
    #This comment is within the body of the main() function.

    name = input('Please provide your full name. ') ###allow someone to name themselves as whatever

    sex = input('What is your gender? Type in "M" for Male, "F" for Female, and "N" for Non-Binary. ')
    sex = sex.upper() ###accounting for lower case inputs by forcing it back into upper case
    accepted_inputs = {'M': ('male', 'He', 'his'),
                       'F': ('female', 'She', 'her'),
                       'N': ('non-binary', 'They', 'their')
                       }
    if sex not in accepted_inputs:
        print('You did not provide a valid input (M/F/N).')
        exit()
    gender = accepted_inputs[sex][0]
    pronoun = accepted_inputs[sex][1]
    poss_pronoun = accepted_inputs[sex][2]

    try:
        date_of_birth = input('What is your date of birth (YYYY-mm-dd)? ')
        date_of_birth_dt = datetime.strptime(date_of_birth, '%Y-%m-%d') ###datetime.datetime
        age = datetime.today() - date_of_birth_dt ###datetime.timedelta
        yrs_old = age.days // 365.25
    except ValueError:
        print('You did not provide your date of birth in the correct format.')
        exit()

    place_of_birth = input('What city where you born in? ')

    try:
        sin = int(input('Please enter your 9-digit Social Security Number (SIN). Do not use spaces, letters or other characters. '))
    except ValueError:
        print('A SIN number only contains numbers. No spaces, letters, or additional characters.')
        exit()

    print(f'{name} is a {yrs_old} year old {gender}. {pronoun} was born in {place_of_birth} and {poss_pronoun} SIN # is {sin}.')


#This comment is NOT within the body of the main() function.

# Do not edit below
if __name__ == '__main__':
    main()
