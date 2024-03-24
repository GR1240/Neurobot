#  Необходимо установить расширение командой  pip install requests
import requests
import time
import json

def cat():    
    url = 'https://api.thecatapi.com/v1/images/search'
    # url = ''
    response = requests.get(url)
    if response.status_code:
        # data = response.json()
        data = json()
        return data.get('image')


if __name__ == '__main__':
    cat()