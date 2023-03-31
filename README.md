[![img](https://github.com/wayscript/wsx-docs/raw/master/.gitbook/assets/deploy.png)](https://app.wayscript.com/deploy/?githubUrl=https://github.com/wayscript/ws-snowflake)

# Spin Up a Snowflake Microservice using WayScript

This template is an example of a web server inside the WayScript X lair environment that can query the Snowflake API. It has 1 endpoint to execute SQL statements across any Warehouse, Database, and Schema

- `POST /<warehouse>/<database>/<schema>` execute SQL against a table
- payload = `{'sql':'SQL STATEMENT'}` 

## Setup

### 1) Save Credentials to Lair

Three values will need to be saved to your secrets file. These values are your `USER`, `PASSWORD`, and `ACCOUNT`.
These values can be found under your admin panel within your snowflake account.

User is your value listed at the top of the admin panel. Password is the value you use as your password to sign into your user. Account is the hyphenated pair of your organization and user. These values can be found dashboard > Admin ( Left side bar ) > Accounts

Next, save the key to the [`.secrets`](https://docs.wayscript.com/platform/lairs/environment-variables#example-.env-and-.secrets-files) file in your Lair. Each of these values will need to be stored in secrets and follow the same case sensativity as they are referenced in your app.py file (call CAPS by default.)

### 2) Deploy application

A trigger should already be pre-configured. [Follow this guide](https://docs.wayscript.com/quickstart-spin-up-server/python/host-a-flask-server#configure-deploy-trigger) to set a trigger in case the trigger isn't present. Press the play button next to the trigger to deploy the flask app.

The app should now be accessible via the endpoint specified next to the trigger. By default, the endpoint is only privately accessible, i.e. it can only be accessed in a browser where you are already logged into WayScript. You can make it publicly accesssible by going to the endpoints tab and setting "Make endpoints publicly accessible" to true. You can learn more about endpoints [here](https://docs.wayscript.com/platform/lairs/endpoints).

### 3) Verify that service is up and working correctly

Visit the `ENDPOINT/status` endpoint. If you get "Snowflake API is connected and working properly", it means the service is running and authenticated to connect with your snowflake account. You can also run the `example.py` by typing `python example.py` inside a WayScript terminal or press the play button in the top right corner of wayscript with `example.py` open.

# Further reading

[Setup a Flask Server (Python)](https://docs.wayscript.com/quickstart-spin-up-server/python/host-a-flask-server)
