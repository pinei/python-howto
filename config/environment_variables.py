# Requirements:
# - pip install python-dotenv
#
# References:
# - Working with enviroment variables
#   https://www.twilio.com/blog/environment-variables-python

import os

from dotenv import load_dotenv
load_dotenv()

secret = os.environ.get('SECRET_TOKEN')
print(f'SECRET_TOKEN: {secret}')

# Try this script with:
# - .env file under `config` folder
# - SECRET_TOKEN=MyToKeN python config/environment_variables.py 