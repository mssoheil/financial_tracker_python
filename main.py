from data_entry import CSV
from get_data import get_date, get_amount, get_category, get_description, DEFAULT_FORMAT


def add():
    csv = CSV("expense.csv")
    csv.initialize_csv(["date", "amount", "category", "description"])

    date = get_date(allowDefault=True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    csv.add_entry(date, amount, category, description)
    print(date, amount, category, description)

def get_transactions():
    csv = CSV("expense.csv")
    csv.initialize_csv(["date", "amount", "category", "description"])
    data_frame = csv.read_data_frame()
    data_frame["date"] = csv.convert_to_datetime(data_frame["date"], DEFAULT_FORMAT)


def main():
    while True:
        print("\n1. Add new transaction")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
             add()
        
        if choice == "2":
            get_transactions()
    pass

if __name__ == "__main__":
    main()
