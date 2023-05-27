import requests
import re

def validate_url(url):
    # Regular expression pattern to validate URLs
    url_pattern = re.compile(r"^(https?://)?([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")
    return url_pattern.match(url)

def process_urls(urls):
    for url in urls:
        url = url.strip()
        if not validate_url(url):
            print(f"Invalid URL: {url}")
            continue

        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        try:
            response = requests.get(url)
            response.raise_for_status()
            print(f"Link {url} works fine")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

source = input("""Enter '1' to enter URLs manually or 
      '2' to read from a text file(The code will read each line of the file as a separate URL): """)

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