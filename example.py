import requests

wayscript_url = 'http://127.0.0.1:5000/'

WAREHOUSE = 'COMPUTE_WH'
DATABASE = 'SNOWFLAKE_SAMPLE_DATA'
SCHEMA = 'TPCDS_SF100TCL'

api_url = wayscript_url + f"{WAREHOUSE}/{DATABASE}/{SCHEMA}"

sql_statement = 'SELECT * FROM INVENTORY WHERE INV_QUANTITY_ON_HAND<3'
payload = {'sql': sql_statement}

response = requests.post(api_url, json=payload)
print(response.content)