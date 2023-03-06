# This service allows users to programmatically interact with your snowflake resources
# Admin user needs to set the credentials of the account to be used via secrets

import os

from flask import Flask, request
import snowflake.connector

# configure user snowflake credentials
# The preferred account identifier includes the name of the account along with its organization (e.g. myorg-account123)
# Find this info in your dashboard > Admin ( Left side bar ) > Accounts
# The ORG will be listed at the top above all the accounts
# The account will be the value in the column 'ACCOUNT' for the account you wish to use. 

# Create snowflake client
def create_snowflake_client():
    USER = os.environ.get('user')
    PASSWORD = os.environ.get('password')
    ACCOUNT = os.environ.get('account')
    conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    )
    cur = conn.cursor()
    return cur

app = Flask(__name__)

@app.route('/<warehouse>/<database>/<schema>', methods=['GET','POST'])
def execute_sql(warehouse, database, schema):
    if request.method == 'POST':

        data = request.get_json()
        if data.get('sql') is None:
            return 'Missing Body Parameter sql'
        
        # Setting active table depending on URL path
        cur = create_snowflake_client()
        cur.execute(f"USE WAREHOUSE {warehouse}")
        cur.execute(f"USE DATABASE {database}")
        cur.execute(f"USE SCHEMA {schema}")

        sql_statement = data.get('sql')
        cur.execute(sql_statement)
        df = cur.fetch_pandas_all()
        json_response = df.to_json()

        return json_response


if __name__ == '__main__':
    app.run()

