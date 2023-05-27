import re
import requests

urls= input("Enter the links here (seprated by spaces): ").split()


url_pattern = re.compile(r"^(https?://)?([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")

for index, url in enumerate(urls):
    if not url_pattern.match(url):
        print(f"Invalid URL: {url}")
        continue

    if not url.startswith("http://") and not url.startswith("https://"):
        urls[index] = "http://" + url
  
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Link {url} works fine")
        
    except requests.exceptions.RequestException as e:
        print(f'Error accessing {url}: {e}')