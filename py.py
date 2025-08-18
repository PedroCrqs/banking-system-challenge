def get_age(function):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        today = datetime.today()
        currentYear = today.year
        year = int(function(*args, **kwargs))
        age = currentYear - year
        return age
    return wrapper

@get_age
def get_birthday_date(year):
    
    return year

age = get_birthday_date(input('Please enter your birthday year: '))
print(age)