import os
from src import parser as ps
from src import functions as f
from src import utils as us
filename = "data.json"
expense_id = 0
data = []

# Creation of a data file were expenses will be stored
if not os.path.isfile(filename):
    open(filename, "w")
    us.write_expense(filename, data)

def main():
    parser, args = ps.parser_args()
    if args.command == "add":
        f.add_expense(filename, args)

    elif args.command == "list":
        f.list_expenses(filename, args)

    elif args.command == "summary":
        f.summary_expenses(filename, args)

    elif args.command == "delete":
        f.delete_expense(filename, args)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()


