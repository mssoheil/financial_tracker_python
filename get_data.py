
from datetime import datetime

def getDate(allowDefault = False):
    date = input("Enter transaction date in yyyy-mm-dd format or Enter for today date: ")
    if allowDefault and not date:
        print("here")
        return datetime.today().strftime("%d-%m-%Y")
    pass

def getCategory():
    pass

def getAmount():
    pass

def getDescription():
    pass