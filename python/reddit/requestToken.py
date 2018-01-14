#!/usr/local/bin/python3
import requests
import requests.auth
import sys
sys.dont_write_bytecode = True
from reddit_creds import *

client_auth = requests.auth.HTTPBasicAuth(reddit_client_id, reddit_client_secret)
post_data = {"grant_type": "password", "username": reddit_username, "password": reddit_password}
headers = {"User-Agent": "3dsDeals-Checkbot/0.1 by conflabermits"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
jresponse = response.json()
print(jresponse["access_token"])
