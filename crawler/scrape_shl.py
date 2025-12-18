import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"

def scrape():
    rows = []
    # loop pagination manually if needed
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.select(".product-card")  # adjust selector
    for p in products:
        name = p.select_one(".title").text.strip()
        url = "https://www.shl.com" + p.select_one("a")["href"]
        desc = p.select_one(".description").text.strip()

        rows.append([name, url, desc])

    with open("shl_raw.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "url", "description"])
        writer.writerows(rows)

if __name__ == "__main__":
    scrape()
