from src import utils as us
import datetime
import pandas as pd


def add_expense(filename, args):
    data = us.read_expense(filename)
    if not data:
        expense_id = 1
    else:
        expense_id = data[-1]["id"] + 1
    desc = args.description
    amount = args.amount
    date = datetime.date.today()
    new_expense = {"id": expense_id, "description": desc, "amount": amount, "date": date.isoformat()}
    data.append(new_expense)
    us.write_expense(filename, data)

def list_expenses(filename, args):
    us.read_expense(filename)
    if args.month != 0:
        filtered_list = filter_month_df(args, filename)
        print(filtered_list)
    else:
        expense_list = pd.read_json(filename)
        print(expense_list.iloc[:])

def delete_expense(filename, args):
    data = us.read_expense(filename)
    infile = any(e["id"] == args.id for e in data)
    if infile:
        expenses_new = [e for e in data if e["id"] != args.id]
        data = expenses_new
        us.write_expense(filename, data)
        print("task deleted")
        return filename, data
    else:
        print("This ID isn't associated with any expense")
        return filename, data

def summary_expenses(filename, args):
    us.read_expense(filename)
    if args.month != 0:
       filtered_list = filter_month_df(args, filename)
       print(filtered_list["amount"].sum())
    else:
        summary = pd.read_json(filename)
        print(f"The sum of all your expenses is {summary["amount"].sum()}.")

def filter_month_df(args, filename):
    expenses_list = pd.read_json(filename)
    expenses_list["date"] = pd.to_datetime(expenses_list["date"])
    filtered_list = expenses_list[expenses_list["date"].dt.month == args.month]
    return filtered_list