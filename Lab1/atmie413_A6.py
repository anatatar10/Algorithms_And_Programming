##Given the current date (day, month, year) and the birthdate of a person (day, month, year) compute the age of the person in number of years.

current_day = int(input("Enter the current day: "))
current_month = int(input("Enter the current month: "))
current_year = int(input("Enter the current year: "))
birthdate_day = int(input("Enter the birthdate day: "))
birthdate_month = int(input("Enter the birthdate month: "))
birthdate_year = int(input("Enter the birthdate year: "))
age = current_year - birthdate_year
if current_month < birthdate_month:
    age = age - 1
elif current_month == birthdate_month:
    if(current_day < birthdate_day):
        age -=1
print(age)
