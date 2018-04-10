import requests
from bs4 import BeautifulSoup

liverpool = requests.get('http://www.liverpoolfc.com/news/first-team')
man_city  = requests.get('https://www.mancity.com/news/first-team')
man_utd   = requests.get('http://www.manutd.com/en/News-And-Features/Club-News.aspx')
tottenham = requests.get('http://www.tottenhamhotspur.com/news/')

