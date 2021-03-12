import requests
import os
import json
from decouple import config
import get_token

def sendMessage(criticals, t):
  # Build message
  message = '# Security Incident Value: ' + t + '\n## Message: ' + criticals
  # Payload for POST Request
  payload={'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vNWM3YmU2MTAtODI4Zi0xMWViLWI0Y2QtYTlhZGFjOTc1YjUy','markdown':message}
  headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' +str(BOT_TOKEN)
  }

  # POST Message
  message = requests.request("POST", webex_url, headers=headers,data=payload)

# Environment Variables
get_token.get_access()
API_TOKEN=config('TOKEN')
BOT_TOKEN=config('BOT_ACCESS_TOKEN')

# API Endpoint
cisco_url = "https://api.cisco.com/security/advisories/latest/10"
webex_url = "https://webexapis.com/v1/messages"

# Payload for GET Request
payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer ' +str(API_TOKEN)
}

# GET Request
response = requests.request("GET", cisco_url, headers=headers, data=payload)

# Filter through Criticals
info = response.json()
criticals = []
for critical in info['advisories']:
  if(critical['sir'] == 'Critical'):
    sendMessage(critical['summary'], critical['sir'])
    criticals.append(critical)

with open('Criticals.json', 'w') as f:
  for item in criticals:
    f.write('%s\n' % item)

#debug print JSON data of Criticals
#print(json.dumps(criticals))
