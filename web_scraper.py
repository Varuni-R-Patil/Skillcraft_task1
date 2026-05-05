import csv
import time
import requests
from bs4 import BeautifulSoup
BASE_URL = "https://books.toscrape.com/catalogue/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"  Error fetching {url}: {e}")
        return [], None
    soup = BeautifulSoup(response.text, "html.parser")
    books = []
    for article in soup.select("article.product_pod"):
        name = article.h3.a["title"]
        price = article.select_one("p.price_color").text.strip().replace("Â", "")
        rating_class = article.p["class"][1]          # e.g. "Three"
        rating = RATING_MAP.get(rating_class, 0)
        availability = article.select_one("p.availability").text.strip()
        books.append({
            "Name": name,
            "Price (£)": price,
            "Rating (out of 5)": rating,
            "Availability": availability,
        })
    next_btn = soup.select_one("li.next a")
    next_url = BASE_URL + next_btn["href"] if next_btn else None
    return books, next_url
def scrape_all(max_pages=5):
    all_books = []
    url = START_URL
    page = 1
    while url and page <= max_pages:
        print(f"  Scraping page {page}...")
        books, url = scrape_page(url)
        all_books.extend(books)
        page += 1
        time.sleep(0.5)
    return all_books
def save_to_csv(books, filename="products.csv"):
    if not books:
        print("No data to save.")
        return
    fieldnames = ["Name", "Price (£)", "Rating (out of 5)", "Availability"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)
    print(f"\n✅ Saved {len(books)} products to '{filename}'")
def main():
    print("=" * 50)
    print("     WEB SCRAPER — Books to Scrape")
    print("=" * 50)
    print("Target: https://books.toscrape.com")
    print("Extracting: Name, Price, Rating, Availability")
    print("-" * 50)
    try:
        pages = int(input("How many pages to scrape? (1-50, default 5): ").strip() or "5")
        pages = max(1, min(pages, 50))
    except ValueError:
        pages = 5
    output_file = input("Output CSV filename (default: products.csv): ").strip() or "products.csv"
    if not output_file.endswith(".csv"):
        output_file += ".csv"
    print(f"\nScraping {pages} page(s)...\n")
    books = scrape_all(max_pages=pages)
    save_to_csv(books, output_file)
    if books:
        print("\nSample data (first 3 entries):")
        print(f"{'Name':<50} {'Price':>10} {'Rating':>8}")
        print("-" * 70)
        for b in books[:3]:
            print(f"{b['Name'][:48]:<50} {b['Price (£)']:>10} {b['Rating (out of 5)']:>8}/5")
if __name__ == "__main__":
    main()
