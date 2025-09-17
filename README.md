# Avalara Customer Bulk Update
Created this program to allow mass-updating of a list of Customers in Avalara, since Avalara (at least the version my company uses) does not have a mass-import tool.  The results are tabulated in a "results.csv" file produced, with a "customerCode" (id for this customer), the field value updated, and the result (Success or Failure with an error explanation). 

The input/source data should be in a .CSV with a "customerCode" column (to be able to tie results to inputs) and a "customFieldValue" column, indicating the value to be set for that customer.  "CUSTOM_FIELD_ID" in "updateCustomers.py" should be replaced with the ID of the custom field to be updated, from Avalara.

## Available Scripts
1. Running this locally, make your Avalara credentials available to the script by listing inside an `.env` file in your project directory as such:
```
AVATAX_USERNAME=<username>
AVATAX_PASSWORD=<password>
COMPANY_ID=<companyid>
```
2. Create a CSV file for Avalara customers to update, and the custom field value to be set on each respective customer.
3. Create and activate a virtual environment:
```
python3 -m venv .venv       # Mac/Linux
python -m venv .venv        # Windows

source .venv/bin/activate   # Mac/Linux
.\venv\Scripts\activate     # Windows
```
4. Install required dependencies:
```
pip install -r requirements.txt
```
5. Run the script:
```
python3 updateCustomers.py
```
