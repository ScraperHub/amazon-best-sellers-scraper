<a href="https://crawlbase.com/signup?utm_source=github&utm_medium=readme&utm_campaign=crawling_api_banner" target="_blank">
  <img src="https://github.com/user-attachments/assets/afa4f6e7-25fb-442c-af2f-b4ddcfd62ab2" 
       alt="crawling-api-cta" 
       style="max-width: 100%; border: 0;">
</a>

# amazon-best-sellers-scraper

## Description

This repository contains a Python-based scraper for extracting Amazon Best Sellers product data. The scraper uses the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) with the Amazon Best Sellers scraper, ensuring seamless data extraction while bypassing Amazon’s anti-bot protections.

➡ Read the full blog [here](https://crawlbase.com/blog/scrape-amazon-best-sellers/) to learn more.

## Scraper Overview

### Amazon Best Sellers Scraper

The `amazon_best_sellers_scraper.py` extracts top-selling product details from the Amazon Best Sellers page, including:

- **Product Title**
- **Price**
- **Customer Review Rating**
- **Number of Reviews**
- **Review Page Link**
- **ASIN**
- **Product Image URL**
- **Product Page Link**
- **Amazon Prime Availability**
- **Product Rank**
- **Categories (Selected & Other Available Categories)**
- **Pagination Details (Current Page & Next Page Number)**

The scraper automatically retrieves structured data in JSON format, making it easy to process and analyze.

## Environment Setup

Ensure Python is installed on your system. Check the version using:

```bash
python --version
```

Install the required dependency:

```bash
pip install crawlbase
```

## Running the Scraper

### 1. Get Your Crawlbase Access Token

- Sign up on [Crawlbase](https://crawlbase.com/signup) to get an API token.
- This token is required to access the Crawling API for bypassing Amazon’s bot protection.

### 2. Update the Scraper with Your Token

Replace "`CRAWLBASE_API_TOKEN`" in the script with your Crawlbase Crawling API Token.

### 3. Run the Scraper

```bash
python amazon_best_sellers_scraper.py
```

The extracted Amazon Best Sellers data will be saved in a JSON file named `amazon_best_sellers.json`.
