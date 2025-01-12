import requests
from bs4 import BeautifulSoup
import json


def check_status(TOKEN):
    # Testing bot response
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)
    result = response.json()

    if result['ok'] == True:
        print('connection stablished...')
    else:
        print('not connected, please try again...')


def send_message(CHAT_ID, TOKEN, message):
    url = (
        f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}')
    response = requests.get(url)
    return response.json()
