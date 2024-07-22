from data_entry import CSV
from get_data import getDate


def add():
    csv = CSV("expense.csv")
    csv.initializeCsv(["date", "amount", "category", "description"])
    date = getDate(allowDefault=True)
    print(date)    


def main():
    while True:
        print("\n1. Add new transaction")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
             add()
    pass

if __name__ == "__main__":
    main()
