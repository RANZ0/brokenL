<h1 align="center"> brokenL</h1>
<p align="center">This program allows you to check for broken links in URLs using Python</p>




## Usage
1. Clone the repository:

```
git clone https://github.com/RANZ0/brokenL.git
```

2. Navigate to the repository's directory:

```
cd brokenL
```
3. Install the requirements to run the program

```
pip3 install -r requirements.py
```

4. Run the program:

```
python3 brokenL.py
```
---
- Follow the prompts to enter the URLs or provide a file path with a list of URLs.

  - If you choose to enter URLs manually, separate each URL with a space.
  - If you choose to read from a text file, make sure the file contains one URL per line.


- The program will validate the URLs, check for broken links, and provide the results.

  - Valid URLs will be checked for broken links.
  - Invalid URLs will be skipped.


- The program will display the status of each link:

  - "Link works fine" - The link is accessible.
  - "Link is offline" - The link is not accessible.
  - "Link has already been visited" - The link has already been checked before.


- Sub-links within the HTML content of the URLs will also be checked recursively.

  - Sub-links that are online will be displayed as "Sub-link is online".
  - Sub-links that are offline will be displayed as "Sub-link is offline".

---
### Tested on

* Ubuntu 23.04
* Windows 10


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
