import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage to scrape
URL = "https://peig.ie/nuacht2/"

# Add headers to make the request appear like it's coming from a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}

# Send a request to fetch the webpage content
response = requests.get(URL, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all headlines inside <span class="underline"> tags
    headlines = soup.find_all("a", class_="uk-link-reset")

    # Extract text from the headlines
    headline_list = [headline.get_text().strip() for headline in headlines]

    # Check if any headlines were found
    print(f"{len(headline_list)} ceannlínte bainte.")
    for headline in headline_list:
        print(headline)  # Print each headline on a new line
        print()  # Add an extra line break between headlines

    # Write headlines to a CSV file
    with open("Ceannlínte.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Ceannlínte"])  # Header row
        for headline in headline_list:
            writer.writerow([headline])

    print("Ceannlínte nuachta scríobadh agus sábháilte go Ceannlínte.csv")

else:
    print(f"Níl an leathanach gréasáin ar fáil. Cód Stádas : {response.status_code}")
