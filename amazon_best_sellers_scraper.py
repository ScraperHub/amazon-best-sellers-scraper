from crawlbase import CrawlingAPI
import json

# Initialize the Crawling API with your Crawlbase token
api = CrawlingAPI({'token': 'CRAWLBASE_API_TOKEN'})

# URL of the Amazon Best Sellers page
amazon_url = 'https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics'

# Options for Crawling API
options = {
    'scraper': 'amazon-best-sellers'
}

response = api.get(amazon_url, options)

# Check if the request was successful
if response.get('status_code') == 200:
    # Loading JSON from response body after decoding byte data
    response_json = json.loads(response['body'].decode('latin1'))

    # Getting Scraper Results
    scraper_result = response_json.get('body', {})

    # Save scraper result to a JSON file
    with open('amazon_best_sellers.json', 'w', encoding='utf-8') as json_file:
        json.dump(scraper_result, json_file, indent=4, ensure_ascii=False)

    print("Scraper response saved to 'amazon_best_sellers.json'")
else:
    print(f"Request failed with status code: {response.get('status_code', 0)}")