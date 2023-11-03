import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url)

response = response.content

html = BeautifulSoup(response, "html.parser")

order_list = html.find("ol")

articles = order_list.find_all("article", class_="product_pod")

for article in articles:
	image = article.find("img")
	title = image.attrs["alt"]
	print(title)