import csv


def get_employees_data(filename):
    filepath = "north_data/" + filename

    try:
        with open(filepath, "r") as f:
            data = []
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
            return data

    except FileNotFoundError:
        return None


def get_customers_data(filename):
    filepath = "north_data/" + filename

    try:
        with open(filepath, "r") as f:
            data = []
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
            return data

    except FileNotFoundError:
        return None


def get_orders_data(filename):
    filepath = "north_data/" + filename

    try:
        with open(filepath, "r") as f:
            data = []
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
            return data

    except FileNotFoundError:
        return None
