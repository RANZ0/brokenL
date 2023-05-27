import requests
import re
import urllib.parse
from bs4 import BeautifulSoup

def validate_url(url):
    # Regular expression pattern to validate URLs
    url_pattern = re.compile(r"^(https?://)?([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/[^?\s]*)?(\?[^?\s]*)?$")
    return url_pattern.match(url)

def process_urls(urls):
    visited_links = set()
    for url in urls:
        url = url.strip()
        if not validate_url(url):
            print(f"Invalid URL: {url}")
            continue

        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        if url in visited_links:
            print(f"Link {url} has already been visited")
            continue

        try:
            response = requests.get(url)
            response.raise_for_status()
            print(f"Link {url} works fine")
            visited_links.add(url)

            # Extract links from the response content
            soup = BeautifulSoup(response.content, 'html.parser')
            ignored_tags = ['head', 'header', 'footer', 'nav']
            links = [link.get('href') for link in soup.find_all('a') if link.get('href') and link.parent.name not in ignored_tags]
            for link in links:
                if link.startswith('#'):
                    # Skip internal page anchors
                    continue

                # Join the extracted link with the base URL if it's a relative path
                if not link.startswith('http://') and not link.startswith('https://'):
                    link = urllib.parse.urljoin(url, link)

                if link not in visited_links:
                    # Check the accessibility of the extracted link
                    try:
                        link_response = requests.get(link)
                        link_response.raise_for_status()
                        print(f"    Sub-link {link} is online")
                        visited_links.add(link)
                    except requests.exceptions.RequestException:
                        print(f"    Sub-link {link} is offline")

        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

source = input("Enter '1' to enter URLs manually or '2' to read from a text file: ")

if source == '1':
    # Manual input
    urls = input("Enter the links here (separated by spaces): ").split()
    process_urls(urls)
elif source == '2':
    # Read from a text file
    file_path = input("Enter the file path: ")
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            process_urls(urls)
    except FileNotFoundError:
        print("File not found.")
else:
    print("Invalid choice.")
