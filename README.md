# pySlack-Console
This is a simple script that will send a message, via webhook, to a slack channel. This script allows you to send a message to a specific channel with a specific username.

## Usage
`py slack.py <USERNAME> <CHANNEL> The message to send`  
For example:  
`py slack.py StatusBot ServerStatus Current server usage: CPU: 32%, MEM: 14%, DISK: 73%.`

## Requirements
- Python (Tested on Python 3)

## Config
Simply open `slack.py` and paste your webhook url on line 5.
