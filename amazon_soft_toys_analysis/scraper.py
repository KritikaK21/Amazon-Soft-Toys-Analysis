import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

# List of user agents to rotate
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
]

# Set headers with random user-agent
headers = {
    'User-Agent': random.choice(user_agents),
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

# Amazon URL to scrape
url = "https://www.amazon.com/s?k=soft+toys"


# Function to fetch the page with retry logic
def fetch_page(url, headers):
    max_retries = 5
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response
            else:
                print(f"Failed with status code: {response.status_code}")
                time.sleep(random.randint(2, 5))  # Delay before retry
                retries += 1
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}. Retrying... ({retries + 1}/{max_retries})")
            retries += 1
            time.sleep(random.randint(2, 5))  # Delay before retry

    print("Max retries exceeded. Aborting.")
    return None


# Fetch the page
response = fetch_page(url, headers)

# If the page was fetched successfully, parse the data
if response:
    soup = BeautifulSoup(response.content, 'html.parser')

    # List to store product data
    product_data = []

    # Find all products
    products = soup.find_all('div', {'data-component-type': 's-search-result'})

    # Extract product details
    for product in products:
        title = product.find('h2')
        price = product.find('span', {'class': 'a-price-whole'})
        rating = product.find('span', {'class': 'a-icon-alt'})
        url = product.find('a', {'class': 'a-link-normal'})['href']

        # Handle missing data
        title = title.text if title else "N/A"
        price = price.text if price else "N/A"
        rating = rating.text if rating else "N/A"
        url = f"https://www.amazon.com{url}" if url else "N/A"

        # Append the data to the list
        product_data.append({
            'Title': title,
            'Price': price,
            'Rating': rating,
            'URL': url
        })

        # Random delay between requests
        time.sleep(random.randint(1, 3))

    # Convert the list of product data into a DataFrame
    df = pd.DataFrame(product_data)

    # Save the data to an Excel file
    df.to_excel('amazon_soft_toys_data.xlsx', index=False)
    print("Data collection complete. Saved to amazon_soft_toys_data.xlsx")
else:
    print("Failed to retrieve the page.")
