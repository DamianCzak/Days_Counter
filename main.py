def main():
    loop = True


    while loop == True:

        error = False
        class Date:
            day: int
            month: int
            year: int
            date: str

        birth_date = Date()
        current_date = Date()
        days_of_your_life = 0

        # Dates input
        birth_date, current_date, error = data_input(birth_date, current_date, error)
        if error == True:
            continue

        # Check if input dates are in the correct scope of numbers
        error = error_elemination(birth_date, current_date)
        if error == True:
            continue

        # Count days since birthday
        days_of_your_life = count_days_of_your_life(birth_date, current_date)

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

def data_input(birth_date, current_date, error):

    try:
        birth_date.day, birth_date.month, birth_date.year = [int(x) for x in input("Enter your date of birth (day month year): ").split()]
    except:
        print("Entered date of birth is not only digits or incorrect format")
        error = True
        return birth_date, current_date, error

    try:
        current_date.day, current_date.month, current_date.year = [int(x) for x in input("Enter current date (day month year): ").split()]
    except:
        print("Entered current date is not only digits or incorrect format")
        error = True
        return birth_date, current_date, error

    return birth_date, current_date, error

def error_elemination(birth_date, current_date):
    error = False

    if (current_date.month > 12 or
        current_date.month < 1):
        print("Incorrect current month")
        error = True
        return error
    elif (birth_date.month > 12 or
          birth_date.month < 1):
        print("Incorrect birth month")
        error = True
        return error
    elif (current_date.day < 1 or
         (current_date.day > 31 and
             (current_date.month in (1, 3, 5, 7, 8, 10, 12))) or
         (current_date.day > 30 and
             (current_date.month in (4, 6, 9))) or
         (current_date.day > 28 and
              current_date.month == 2) or
         ((current_date.day > 29 and
              current_date.month == 2) and
                  (current_date.year % 400 == 0 or
                  (current_date.year % 4 == 0 and
                   current_date.year % 100 != 0)))):
        print("Incorrect current day")
        error = True
        return error
    elif (birth_date.day < 1 or
         (birth_date.day > 31 and
             (birth_date.month in (1, 3, 5, 7, 8, 10, 12))) or
         (birth_date.day > 30 and
             (birth_date.month in (4, 6, 9))) or
         (birth_date.day > 28 and
              birth_date.month == 2) or
         ((birth_date.day > 29 and
              birth_date.month == 2) and
                  (birth_date.year % 400 == 0 or
                  (birth_date.year % 4 == 0 and
                   birth_date.year % 100 != 0)))):
        print("Incorrect birth day")
        error = True
        return error
    elif (birth_date.year > current_date.year or
          (birth_date.year == current_date.year and
              birth_date.month > current_date.month) or
         (birth_date.year == current_date.year and
          birth_date.month == current_date.month and
          birth_date.day > current_date.day)):
        print("You have not born yet")
        error = True
        return error
    elif (birth_date.year == current_date.year and
          birth_date.month == current_date.month and
          birth_date.day == current_date.day):
        print("You were born today")
        error = True
        return error
    else:
        return error

def count_days_of_your_life(birth_date, current_date):
    months_of_the_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Counter for days in between year of birth and current year (years_in_between_days)
    temp_birth_year = birth_date.year
    leap_year_days = 0
    while temp_birth_year < current_date.year:
        if (birth_date.year % 400 == 0 or
            birth_date.year % 4 == 0 and
            birth_date.year % 100 != 0):
            leap_year_days += 1
        temp_birth_year += 1
    years_in_between_days = ((current_date.year-birth_date.year-1)*365)+leap_year_days

    # Counter for days in the year of birth
    months_counter = birth_date.month
    birth_year_days = 0
    while months_counter <= 12:
        birth_year_days = birth_year_days + months_of_the_year[months_counter-1]
        months_counter += 1
    if ((birth_date.month == 1 or
         birth_date.month == 2) and
            birth_date.year % 400 == 0 or
            (birth_date.year % 4 == 0 and
            birth_date.year % 100 != 0)):
        birth_year_days += 1
    birth_year_days -= birth_date.day

    # Counter for days in the current year
    months_counter = current_date.month
    current_year_days = 0
    while months_counter >= 2:
        current_year_days = current_year_days + months_of_the_year[months_counter-2]
        months_counter -= 1
    if ((current_date.month in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) and
            current_date.year % 400 == 0 or
            (current_date.year % 4 == 0 and
            current_date.year % 100 != 0)):
        current_year_days += 1
    current_year_days += current_date.day

    days_of_your_life = birth_year_days + current_year_days + years_in_between_days
    return days_of_your_life

main()