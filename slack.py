import sys
import json
import requests

webhook_url = 'full webhook url'
slack_data = {'text': " ".join(sys.argv[3:]), 'username': sys.argv[1], 'channel': sys.argv[2]}
response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
)