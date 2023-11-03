import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url)

response = response.content

html = BeautifulSoup(response, "html.parser")

print(html)
