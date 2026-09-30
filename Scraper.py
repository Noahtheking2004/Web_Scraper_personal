import requests
from bs4 import BeautifulSoup
import csv

# change based off of website
url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article", class_="product_pod")

rows = []
# change for webstie
for book in books:
    # title
    title = book.find("h3").find("a")["title"]

    # star rating
    star_rating = book.find("p", class_="star-rating")["class"][1]

    #availability
    availability = book.find("p", class_="instock availability").text.strip()

    #Check price
    price = book.find("p", class_="price_color").text.strip()

    rows.append([title, star_rating, availability, price])

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Star Rating", "Availability", "Price"])
    writer.writerow([title, star_rating, availability, price])

print(f"saved {len(rows)} books to csv")

