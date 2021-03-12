import requests
import os
from decouple import config

# Environment Variables
API_CLIENT_ID = config('CLIENT_ID')
API_CLIENT_SECRET = config('CLIENT_SECRET')

# API Endpoint
url = "https://cloudsso.cisco.com/as/token.oauth2"


# Payload for POST Request
payload='client_id=' + str(API_CLIENT_ID) + '&client_secret=' + str(API_CLIENT_SECRET) + '&grant_type=client_credentials'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'PF=SEURVZDHeR5ekkfJaEkVhx'
}

def get_access():
  # POST Request
  response = requests.request("POST", url, headers=headers, data=payload)

  # Parsing to JSON
  info = response.json()

  # debug || show JSON text of client credentials
  #print(response.text)

  access = info['access_token']
  #debug || show text of BEARER TOKEN
  #print(access)

  # 1. Open file
  # 2. Read all lines
  # 3. Delete last line
  # 4. Add TOKEN Variable
  with open('.env', 'r') as f:
    lines = f.readlines()
    print(lines)
    lines = lines[:-1]
    print(lines)
    lines.append('TOKEN='+ str(access))
    print(lines)
    
  # 5. Write file to save it
  with open('.env', 'w') as f:
    f.writelines(lines)