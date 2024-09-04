from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# List of URLs
urls = {
    "Amazon": "https://www.amazon.eg/-/en/SAMSUNG-Android-Smartphone-Storage-Titanium/dp/B0CQYZ87TQ/ref=cs_sr_dp_3?crid=1CBXHXW5ZLNMO&dib=eyJ2IjoiMSJ9.Qvm_W2yOC7HzeDhErLDgMdcfaP8CLjieXEWcA0N3PLESht7Sqn-QkMa4hy-OnlCbCWkIM24Syeo55A6ksIhZoED-x-7K5G2FaG2nAtZc1XdKypcfv877KaIr6XjNgTHnWrWvxpWAOBLP3xoQZYqiRm35Bq1w82RCYBNCvIYhx6gXYcjOFHcWcPevqL8F_boz60AtqcbyJF_q9v5k8-FDcgRaqKC3leG1rPuyPi5zwwiHzut-zEIGNKucV7jgBC9Utmpk9LV4iKPWYD6zYz88Q4Fqkc9plfQiyHm1vdhhHY4.0p5dC41inE-gRCfC4Cfw0dQtSclGDIRri6zoZAt0A8Q&dib_tag=se&keywords=s24%2Bultra%2B256&qid=1725406415&sprefix=s24%2Bultra%2B256%2Caps%2C139&sr=8-3&th=1",
    "Noon": "https://www.noon.com/egypt-ar/galaxy-s24-ultra-dual-sim-titanium-gray-12gb-ram-256gb-5g-middle-east-version/N70035206V/p/?o=cb44deb34aeab68b",
    "B.TECH": "https://btech.com/ar/samsung-galaxy-s24-ultra-256gb-12gb-ram-dual-sim-5g-grey.html#:~:text=%D8%A7%D8%B9%D8%B1%D9%81%20%D8%B3%D8%B9%D8%B1%20%D9%88%20%D9%85%D9%88%D8%A7%D8%B5%D9%81%D8%A7%D8%AA%20%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84%20%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%D8%AC%20%D8%AC%D8%A7%D9%84%D9%83%D8%B3%D9%8A%20S24%20%D8%A7%D9%84%D8%AA%D8%B1%D8%A7%20%D8%A8%D8%B4%D8%B1%D9%8A%D8%AD%D8%AA%D9%8A%D9%86%D8%8C",
    "2b": "https://2b.com.eg/en/samsung-galaxy-s24-ultra-12gb-ram-256gb-gray-titanium.html",
}

# Function to get price from Amazon
def get_price_from_amazon(driver):
    time.sleep(2)  # Wait for the page to load
    try:
        # Find the price element using CSS selector
        price_element = driver.find_element(By.CSS_SELECTOR, "span.a-price-whole")
        if price_element:
            return price_element.text.strip()
    except Exception as e:
        print(f"Error fetching price from Amazon: {e}")
    return None

# Function to get price from Noon
def get_price_from_noon(driver):
    time.sleep(2)  # Wait for the page to load
    try:
        # Find the price element using CSS selector
        price_element = driver.find_element(By.CSS_SELECTOR, "div.priceNow")
        if price_element:
            return price_element.text.strip()
    except Exception as e:
        print(f"Error fetching price from Noon: {e}")
    return None

# Function to get price from B.TECH
def get_price_from_btech(driver):
    time.sleep(2)  # Wait for the page to load
    try:
        # Find the price element using CSS selector
        price_element = driver.find_element(By.CSS_SELECTOR, "span.price")
        if price_element:
            return price_element.text.strip()
    except Exception as e:
        print(f"Error fetching price from B.TECH: {e}")
    return None

# Function to get price from 2b
def get_price_from_2b(driver):
    time.sleep(2)  # Wait for the page to load
    try:
        # Find the price element using CSS selector
        price_element = driver.find_element(By.CSS_SELECTOR, "span.price")
        if price_element:
            return price_element.text.strip()
    except Exception as e:
        print(f"Error fetching price from 2b: {e}")
    return None

# Dictionary of parsers for each site
parsers = {
    "Amazon": get_price_from_amazon,
    "Noon": get_price_from_noon,
    "B.TECH": get_price_from_btech,
    "2b": get_price_from_2b,
}

# Loop through URLs and scrape prices
for site, url in urls.items():
    driver.get(url)  # Navigate to the URL

    # Extract the price using the corresponding function
    price = parsers[site](driver)

    if price:
        print(f"The price on {site} is: {price}")
    else:
        print(f"Could not find the price on {site}.")

# Close WebDriver
driver.quit()