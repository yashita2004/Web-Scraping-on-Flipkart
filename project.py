import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

# Send a GET request to the URL
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Lists to store data
products = []
prices = []
ratings = []

# Extract data
all_laptops = soup.findAll('a', href=True, attrs={'class': '_31qSD5'})

for laptop in all_laptops:
    name = laptop.find('div', attrs={'class': '_3wU53n'})
    price = laptop.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    rating = laptop.find('div', attrs={'class': 'hGSR34'})
    
    if name and price and rating:
        products.append(name.text.strip())
        prices.append(price.text.strip())
        ratings.append(rating.text.strip())

# Create a DataFrame
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})

# Save to CSV
df.to_csv('laptop_details.csv', index=False, encoding='utf-8')

print("Scraping completed and data saved to laptop_details.csv")