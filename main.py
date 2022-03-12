# This was made by Ivano
# Date: 3/12/2022
# Explain: it sends date in chat, when someone pass mouse on it it shows like 1/1/1999, able to change string below.

import requests

token = input("Token: ")
channelid = input("Channel ID: ")

string = "<t:-531763200:R>"
data = { 'content': string }
headers = { 'authorization': token }
url = f"https://discord.com/api/v9/channels/{channelid}/messages"

xlol = requests.post(url, data=data, headers=headers)