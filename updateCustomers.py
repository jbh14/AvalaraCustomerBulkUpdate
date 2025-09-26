import requests
import os
from requests.auth import HTTPBasicAuth
from readCustomFieldValuesFromCSV import read_custom_field_values_from_csv
from writeResultToCSV import write_result_to_csv
from dotenv import load_dotenv

INPUT_CSV_FILE = "updateList.csv" # needs to be in the same directory as this script
OUTPUT_CSV_FILE = "results.csv" # will be created in the same directory as this script

# get env variables for Avatax credentials
load_dotenv()
if not os.getenv("AVATAX_USERNAME"):
    raise ValueError("AVATAX_USERNAME is not set in the environment variables")
if not os.getenv("AVATAX_PASSWORD"):
    raise ValueError("AVATAX_PASSWORD is not set in the environment variables")

# Replace these with your AvaTax credentials
AVATAX_USERNAME = os.getenv("AVATAX_USERNAME")
AVATAX_PASSWORD = os.getenv("AVATAX_PASSWORD")

# same with Company ID
if not os.getenv("COMPANY_ID"):
    raise ValueError("COMPANY_ID is not set in the environment variables")
COMPANY_ID = os.getenv("COMPANY_ID")

# AvaTax base URL (use https://sandbox-rest.avatax.com for sandbox testing)
BASE_URL = "https://rest.avatax.com"

# read custom field values from CSV - this is a nested dict: { customer_id: { field_id: field_value, ... }, ... }
custom_field_values = read_custom_field_values_from_csv(INPUT_CSV_FILE)
print(f"Custom field values to update: {custom_field_values}")

for customer_code, custom_fields in custom_field_values.items():
    print(f"Customer Code: {customer_code}")
    print(f"Custom Fields to Update: {custom_fields}")
    
    # Endpoint for updating a single customer's custom fields
    url = f"{BASE_URL}/api/v2/companies/{COMPANY_ID}/customers/{customer_code}/custom-fields"

    # payload (only include fields you want to update for custom fields route)
    payload = {
        "customFields": [
            { "id": field_id, "value": value } for field_id, value in custom_fields.items()
        ]
    }
    print(f"Payload: {payload}")    

    # Send PUT request to update customer
    response = requests.put(
        url,
        json=payload,
        auth=HTTPBasicAuth(AVATAX_USERNAME, AVATAX_PASSWORD)
    )

    # log result to CSV
    if response.status_code == 200:
        print("Customer updated successfully:")
        print(response.json())
        write_result_to_csv(OUTPUT_CSV_FILE, customer_code, custom_fields, "Success")
    else:
        print(f"Error {response.status_code}: {response.text}")
        write_result_to_csv(OUTPUT_CSV_FILE, customer_code, custom_fields, f"Error {response.status_code}: {response.text}")
