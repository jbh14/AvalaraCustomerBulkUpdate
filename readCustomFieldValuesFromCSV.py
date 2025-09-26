import csv

# Function to read custom field values to set on Avalara Customers from CSV into dict:
# { customer_id: { field_id: field_value, ... }, ... }
def read_custom_field_values_from_csv(
    csv_filename,
    customer_id_file_header="customerCode",
) -> dict:
    custom_field_values = {}

    with open(csv_filename, mode="r", encoding="utf-8-sig", errors="replace") as file:
        reader = csv.DictReader(file)  # Reads CSV into a dictionary format

        for row in reader:
            customer_id = row[customer_id_file_header]
            if not customer_id:
                continue

            # Initialize inner dict if not already there
            if customer_id not in custom_field_values:
                custom_field_values[customer_id] = {}

            # Loop through every column in the row except the customer_id column
            for field_id, field_value in row.items():
                if field_id == customer_id_file_header:
                    continue
                # Add field_id → value
                custom_field_values[customer_id][field_id] = field_value

    return custom_field_values