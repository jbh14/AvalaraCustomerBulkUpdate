import csv

# Function to read custom field values to set on Avalara Customers from CSV 
def read_custom_field_values_from_csv(csv_filename, customer_id_file_header="customerCode", custom_field_file_header="customFieldValue") -> list:
    custom_field_values = dict()
    with open(csv_filename, mode="r", encoding="utf-8-sig", errors="replace") as file:
        reader = csv.DictReader(file)  # Reads CSV into a dictionary format
        for row in reader:
            print(f"Row: {row}")
            print(f"Customer ID: {row[customer_id_file_header]}")
            print(f"Row Custom Field Value: {row[custom_field_file_header]}")
            custom_field_values[row[customer_id_file_header]] = row[custom_field_file_header]

    return custom_field_values