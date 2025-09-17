import csv
import os

def write_result_to_csv(csv_filename, customer_id, custom_field_value, result,
                        customer_id_file_header="customerCode", custom_field_file_header="customFieldValue", result_file_header="result"):

    # see if file exists and if it's empty
    file_exists = os.path.exists(csv_filename)
    file_empty = not file_exists or os.path.getsize(csv_filename) == 0
    print(f"File exists: {file_exists}, File empty: {file_empty}")

    with open(csv_filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[customer_id_file_header, custom_field_file_header, result_file_header])

        # Only write header if file is empty
        if file_empty:
            print("Writing header to CSV")
            writer.writeheader()

        # Write the row to the CSV file
        print("Writing to CSV:", {
            customer_id_file_header: customer_id,
            custom_field_file_header: custom_field_value,
            result_file_header: result
        })
        writer.writerow({
            customer_id_file_header: customer_id,
            custom_field_file_header: custom_field_value,
            result_file_header: result
        })