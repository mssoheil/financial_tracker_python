from data_entry import CSV
from get_data import get_date, get_amount, get_category, get_description


def add():
    csv = CSV("expense.csv")
    csv.initialize_csv(["date", "amount", "category", "description"])

    date = get_date(allowDefault=True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    csv.add_entry(date, amount, category, description)
    print(date, amount, category, description)   

def get_transaction():
    csv = CSV("expense.csv")
    csv.initialize_csv(["date", "amount", "category", "description"])
    data_frame = csv.read_data_frame()


def main():
    while True:
        print("\n1. Add new transaction")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
             add()
    pass

if __name__ == "__main__":
    main()
