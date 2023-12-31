import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

for i in range(1, 4):
	url = f"https://books.toscrape.com/catalogue/page-{i}.html"

	response = requests.get(url)
	response = response.content

	html = BeautifulSoup(response, "html.parser")

	order_list = html.find("ol")

	articles = order_list.find_all("article", class_="product_pod")


	for article in articles:
		image = article.find("img")

		title = image.attrs["alt"]

		star = article.find("p")
		star = star["class"][1]

		price = article.find('p', class_= "price_color").text
		price = float(price[1:])

		books.append([title, price, star])


data_frame = pd.DataFrame(books, columns=['Title', 'Price', 'Star Rating'])

data_frame.to_csv('Books.csv')