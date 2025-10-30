import csv
def fetch_value_from_csv(filename, search_value, target_column_index):
    with open(filename, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row and row[0] == search_value:
                if target_column_index < len(row):
                    return row[target_column_index]
                else:
                    print(f"Error: Target column index {target_column_index} is out of bounds for row: {row}")
                    return None
    return None