import requests
from bs4 import BeautifulSoup

url= "https://www.sofascore.com/chelsea-west-ham-united/MsN#11352418"

response= requests.get(url,
                      headers={
                          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                      })
response.status_code

soup= BeautifulSoup(response.text,'html.parser')


headers = {
    'authority': 'api.sofascore.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.5',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"ad14a22f55"',
    'origin': 'https://www.sofascore.com',
    'referer': 'https://www.sofascore.com/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

response = requests.get('https://api.sofascore.com/api/v1/event/11352418/shotmap', headers=headers)

headers['if-Modified-Since']= 'Sat 23 Aug 2023 00:00:00 GMT'

response = requests.get('https://api.sofascore.com/api/v1/event/11352418/shotmap', headers=headers)
response.status_code

shots= response.json()

shots
