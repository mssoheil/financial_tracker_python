
from datetime import datetime

DEFAULT_FORMAT = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(allowDefault = False):
    date = input("Enter transaction date in dd-mm-yyyy format or Enter for today date: ")
    if allowDefault and not date:
        return datetime.today().strftime(DEFAULT_FORMAT)
    
    try:
        validDate = datetime.strptime(date, DEFAULT_FORMAT)
        return validDate.strftime(DEFAULT_FORMAT)
    
    except ValueError:
        print("Invalid date format, the date format should be in dd-mm-yyyy")
        return get_date(allowDefault)

def get_category():
    category = input("Enter category ('I' for Income or 'E' for Expense): ").upper()

    try:
        if category not in CATEGORIES:
            raise ValueError("Invalid category. Category should be either I or E ")
        
        return CATEGORIES[category]
    
    except ValueError as e:
        print(e)
        return get_category()

def get_amount():
    try:
        enteredAmount = input("Enter amount: ")

        if not enteredAmount:
            raise ValueError("Amount can not be empty") 

        if not enteredAmount.isnumeric():
            raise ValueError("Amount should be number") 

        amount = float(enteredAmount)

        if amount <= 0:
            raise ValueError("Amount must be larger than 0")
             
        return amount
    
    except ValueError as e:
        print(e)
        return get_amount()


def get_description():
    description = input("Enter description: ")

    return description