import json

def write_expense(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found or corrupted, please delete manually")
        raise SystemExit

def read_expense(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found or corrupted, please delete manually")
        raise SystemExit


