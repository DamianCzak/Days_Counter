def main():
    loop = True
    error = False
    birth_day, birth_month, birth_year = 0, 0, 0
    current_day, current_month, current_year = 0, 0, 0
    days_of_your_life = 0

    while loop == True:
        # Dates input
        birth_day, birth_month, birth_year, current_day, current_month, current_year, error = data_input(birth_day, birth_month, birth_year, current_day, current_month, current_year, error)
        # Check if input dates are in the correct scope of numbers
        error = error_elemination(birth_day, birth_month, birth_year, current_day, current_month, current_year)
        # Count days since birthday
        days_of_your_life = counter(birth_day, birth_month, birth_year, current_day, current_month, current_year, days_of_your_life)

        if error == False:
            if days_of_your_life == 1:
                print("You have " + str(days_of_your_life) + " day")
            else:
                print("You have " + str(days_of_your_life) + " days")

        repeat_question = input("Would you like to repeat (Y/N): ")
        if repeat_question.upper() == 'Y':
            loop = True
        else:
            loop = False

def data_input(birth_day, birth_month, birth_year, current_day, current_month, current_year, error):
    birth_date = input("Enter your date of birth (day month year): ")
    current_date = input("Enter current date (day month year): ")

    # Check if input dates are digits
    if (birth_date.replace(" ","").isdigit() == False or
        current_date.replace(" ","").isdigit() == False):
        error = True
        print("Incorrect date")
        return birth_day, birth_month, birth_year, current_day, current_month, current_year, error

    birth_date = birth_date.split()
    current_date = current_date.split()

    # Check if input dates are in the correct format
    if (len(birth_date) != 3  or
        len(current_date) != 3):
        error = True
        print("Incorrent date")
        return birth_day, birth_month, birth_year, current_day, current_month, current_year, error
    else:
        birth_day = int(birth_date[0])
        birth_month = int(birth_date[1])
        birth_year = int(birth_date[2])

        current_day = int(current_date[0])
        current_month = int(current_date[1])
        current_year = int(current_date[2])

    return birth_day, birth_month, birth_year, current_day, current_month, current_year, error

def error_elemination(birth_day, birth_month, birth_year, current_day, current_month, current_year):
    error = False

    if (current_month > 12 or
        current_month < 1):
        print("Incorrect current month")
        error = True
        return error
    elif (birth_month > 12 or
          birth_month < 1):
        print("Incorrect birth month")
        error = True
        return error
    elif (current_day < 1 or
         (current_day > 31 and
             (current_month == 1 or
              current_month == 3 or
              current_month == 5 or
              current_month == 7 or
              current_month == 8 or
              current_month == 10 or
              current_month == 12)) or
         (current_day > 30 and
             (current_month == 4 or
              current_month == 6 or
              current_month == 9)) or
         (current_day > 28 and
              current_month == 2) or
         ((current_day > 29 and
              current_month == 2) and
                  (current_year % 400 == 0 or
                  (current_year % 4 == 0 and
                   current_year % 100 != 0)))):
        print("Incorrect current day")
        error = True
        return error
    elif (birth_day < 1 or
         (birth_day > 31 and
             (birth_month == 1 or
              birth_month == 3 or
              birth_month == 5 or
              birth_month == 7 or
              birth_month == 8 or
              birth_month == 10 or
              birth_month == 12)) or
         (birth_day > 30 and
             (birth_month == 4 or
              birth_month == 6 or
              birth_month == 9)) or
         (birth_day > 28 and
              birth_month == 2) or
         ((birth_day > 29 and
              birth_month == 2) and
                  (birth_year % 400 == 0 or
                  (birth_year % 4 == 0 and
                   birth_year % 100 != 0)))):
        print("Incorrect birth day")
        error = True
        return error
    elif (birth_year > current_year or
          (birth_year == current_year and
              birth_month > current_month) or
         (birth_year == current_year and
          birth_month == current_month and
          birth_day > current_day)):
        print("You have not born yet")
        error = True
        return error
    elif (birth_year == current_year and
          birth_month == current_month and
          birth_day == current_day):
        print("You were born today")
        error = True
        return error
    else:
        return error

def counter(birth_day, birth_month, birth_year, current_day, current_month, current_year, days_of_your_life):
    months_of_the_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #Counter for days in between year of birth and current year (years_in_between_days)
    temp_birth_year = birth_year
    leap_year_days = 0
    while temp_birth_year < current_year:
        if (birth_year % 400 == 0 or
            birth_year % 4 == 0 and
            birth_year % 100 != 0):
            leap_year_days += 1
        temp_birth_year += 1
    years_in_between_days = ((current_year-birth_year-1)*365)+leap_year_days

    #Counter for days in the year of birth
    months_counter = birth_month
    birth_year_days = 0
    while months_counter <= 12:
        birth_year_days = birth_year_days + months_of_the_year[months_counter-1]
        months_counter += 1
    if ((birth_month == 1 or
         birth_month == 2) and
            birth_year % 400 == 0 or
            (birth_year % 4 == 0 and
            birth_year % 100 != 0)):
        birth_year_days += 1
    birth_year_days -= birth_day

    #Counter for days in the current year
    months_counter = current_month
    current_year_days = 0
    while months_counter >= 2:
        current_year_days = current_year_days + months_of_the_year[months_counter-2]
        months_counter -= 1
    if ((current_month == 3 or
         current_month == 4 or
         current_month == 5 or
         current_month == 6 or
         current_month == 7 or
         current_month == 8 or
         current_month == 9 or
         current_month == 10 or
         current_month == 11 or
         current_month == 12) and
            current_year % 400 == 0 or
            (current_year % 4 == 0 and
            current_year % 100 != 0)):
        current_year_days += 1
    current_year_days += current_day

    days_of_your_life = birth_year_days + current_year_days + years_in_between_days
    return days_of_your_life

main()