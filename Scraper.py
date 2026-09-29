import requests
from bs4 import BeautifulSoup

# change based off of website
url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article", class_="product_pod")
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

    print(f"Title: {title}")
    print(f"Star Rating: {star_rating}")
    print(f"Availability: {availability}")
    print(f"Price: {price}")
    print("-" * 40)

