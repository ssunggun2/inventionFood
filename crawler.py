import requests
from bs4 import BeautifulSoup

url = 'https://www.10000recipe.com/recipe/6940325'
header = {'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')} 

response = requests.get(url=url, headers=header)
bs = BeautifulSoup(response.text, 'html.parser')

