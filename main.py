import json
from bs4 import BeautifulSoup
import requests
from telegram_bot import check_status, send_message


def read_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        return data


# Primary keys
data = read_json('config.json')
TOKEN = data['TOKEN']
CHAT_ID = data['CHAT_ID']


message = "Hola juanma"


check_status(TOKEN)
send_message(CHAT_ID, TOKEN, message)
