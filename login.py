import robin_stocks.robinhood as r
import os
import json


"""
Login initially to save the pickle in ~/.tokens. 
After it, it will be used by subsequent run of the script

$ export rh_email=***
$ export rh_pass=****
"""

rs_email = os.getenv('rh_email')
rh_pass = os.getenv('rh_pass')
print('rs_email:', rs_email)
print('rh_pass: ****')
login = r.login(os.getenv('rh_email'),os.getenv('rh_pass'))
print(json.dumps(login, indent=4))