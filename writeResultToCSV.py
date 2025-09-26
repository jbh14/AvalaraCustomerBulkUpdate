import csv
import os

def write_result_to_csv(
    csv_filename,
    customer_id,
    field_values: dict,
    result,
    customer_id_file_header="customerCode",
    result_file_header="result"
):
    """
    Writes results with one row per customer.
    Each custom field gets its own column in the CSV.
    """
    # Collect existing header (if any)
    existing_fields = []
    if os.path.exists(csv_filename) and os.path.getsize(csv_filename) > 0:
        with open(csv_filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            existing_fields = reader.fieldnames or []

    # Determine new header (merge existing + new fields)
    all_field_ids = list(field_values.keys())
    fieldnames = [customer_id_file_header] + all_field_ids + [result_file_header]

    # Merge with existing if needed
    for f in existing_fields:
        if f not in fieldnames:
            fieldnames.insert(-1, f)  # insert before "result"

    with open(csv_filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Only write header if file is empty
        file_empty = not existing_fields
        if file_empty:
            print("Writing header to CSV:", fieldnames)
            writer.writeheader()

        # Build the row
        row = {customer_id_file_header: customer_id, result_file_header: result}
        row.update(field_values)  # Add fieldId:value pairs

        print("Writing row:", row)
        writer.writerow(row)