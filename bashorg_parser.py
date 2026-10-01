import requests
from bs4 import BeautifulSoup

quotes_array = []

response = requests.get("https://башорг.рф")
soup = BeautifulSoup(response.text, "html.parser")

quotes_points = soup.find_all(class_="quotes")

for quotes_point in quotes_points:
    quotes = quotes_point.find_all(class_="quote")
    for quote in quotes:
        quote_text = quote.find("div", class_="quote__body")
        for br in quote_text.find_all("br"):
            br.replace_with("\n")
        quotes_array.append(quote_text.getText().strip())

with open("bashorg_quotes.txt", "w", encoding="utf-8") as f:
    for q in quotes_array:
        f.write(q + "\n\n---\n\n")