import argparse

def parser_args():
    parser = argparse.ArgumentParser(description="This program helps you to track your expenses.")
    subparsers = parser.add_subparsers(dest="command")
    # add expense
    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("--description", required=True, help="adds a description to your expense")
    add_parser.add_argument("--amount", required=True, default=0, type=float, help="adds the amount to your expense")
    # list expense
    list_parser = subparsers.add_parser("list", help="lists your expenses")
    list_parser.add_argument("--month", type=int, default=0, help="Filters by a month")
    # summary expense
    sum_parser = subparsers.add_parser("summary", help="print the sum of all your expenses")
    sum_parser.add_argument("--month", type=int, default=0, help="Filters by a month")
    # delete expense
    del_parser = subparsers.add_parser("delete", help="deletes an expense")
    del_parser.add_argument("--id", type=int, required=True, default=None, help="id of your expense")

    args = parser.parse_args()
    return parser, args

