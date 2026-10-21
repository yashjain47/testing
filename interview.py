"""



Part 1 — Web Scraping Fundamentals
1. What is web scraping?

Web scraping is the process of programmatically extracting information from web pages.

Typical flow:

Website
   ↓
HTTP Request
   ↓
HTML Response
   ↓
Parse HTML
   ↓
Extract required data
   ↓
Store data


------------------------------------------------------------------------------------------------
2. Which Python libraries are commonly used for web scraping?

Common libraries:

requests
BeautifulSoup
Scrapy
Selenium
Playwright
lxml

For basic static HTML scraping:

requests + BeautifulSoup

is very common.




------------------------------------------------------------------------------------------------
3. What is BeautifulSoup?

BeautifulSoup is a Python library used to parse HTML and XML documents.

Example:

from bs4 import BeautifulSoup

html = "<h1>Hello</h1>"

soup = BeautifulSoup(html, "html.parser")

print(soup.h1.text)

Output:

Hello



------------------------------------------------------------------------------------------------
4. What is the difference between Selenium and BeautifulSoup?
Selenium	BeautifulSoup
Browser automation	HTML parsing
Can interact with UI	Doesn't interact with UI
Handles JavaScript-rendered pages	Doesn't execute JavaScript
Click/type/scroll	Extract HTML data
More resource intensive	Lightweight

For an SDET:

Static page → requests + BeautifulSoup

Dynamic page → Selenium/Playwright



------------------------------------------------------------------------------------------------
5. What is the difference between requests and BeautifulSoup?

requests downloads the web page.

BeautifulSoup parses the downloaded HTML.

requests
   ↓
HTML
   ↓
BeautifulSoup
   ↓
Extract data

Example:

import requests
from bs4 import BeautifulSoup

response = requests.get(url)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)


------------------------------------------------------------------------------------------------
Part 2 — Requests
6. How do you send a GET request?
import requests

response = requests.get(
    "https://example.com"
)

print(response.status_code)
print(response.text)


------------------------------------------------------------------------------------------------
7. How do you check whether a request succeeded?
response = requests.get(url)

if response.status_code == 200:
    print("Success")

Better:

response.raise_for_status()

This raises an exception for HTTP error responses.



------------------------------------------------------------------------------------------------
8. What is HTTP status code 200?

200 means the request was successful.

Common codes:

200 → OK
201 → Created
301 → Redirect
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
429 → Too Many Requests
500 → Server Error



------------------------------------------------------------------------------------------------
9. How do you add headers?
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers
)

Headers can be necessary when a server behaves differently depending on the client.



------------------------------------------------------------------------------------------------
10. Why is User-Agent important?

A server can use the User-Agent to identify the type of client making the request.

For example:

Browser
Mobile browser
Bot
Python client

For legitimate scraping, you should identify yourself appropriately and respect the site's terms and robots policies.



------------------------------------------------------------------------------------------------
Part 3 — BeautifulSoup
11. How do you create a BeautifulSoup object?
from bs4 import BeautifulSoup

soup = BeautifulSoup(
    html,
    "html.parser"
)


------------------------------------------------------------------------------------------------
12. What parsers can BeautifulSoup use?

Common options include:

html.parser
lxml
html5lib

Example:

BeautifulSoup(html, "lxml")


------------------------------------------------------------------------------------------------
13. How do you find the first <h1>?
heading = soup.find("h1")

print(heading.text)


------------------------------------------------------------------------------------------------
14. What does find() do?

find() returns the first matching element.

element = soup.find("div")


------------------------------------------------------------------------------------------------
15. What does find_all() do?

It returns all matching elements.

elements = soup.find_all("div")

for element in elements:
    print(element.text)
    
    
------------------------------------------------------------------------------------------------
16. Difference between find() and find_all()?
find()
    ↓
first matching element

find_all()
    ↓
all matching elements

This is one of the most common interview questions.


------------------------------------------------------------------------------------------------
17. How do you find an element by class?
element = soup.find(
    "div",
    class_="product"
)

Note:

class_

is used because class is a Python keyword.


------------------------------------------------------------------------------------------------
18. How do you find an element by ID?
element = soup.find(
    id="product"
)



------------------------------------------------------------------------------------------------
19. How do you find all elements with a particular class?
products = soup.find_all(
    "div",
    class_="product"
)


------------------------------------------------------------------------------------------------
20. How do you extract text?
text = element.get_text()

You can remove extra whitespace:

text = element.get_text(
    strip=True
)



------------------------------------------------------------------------------------------------
Part 4 — Attributes
21. How do you extract an attribute?

HTML:

<a href="/products">Products</a>

Python:

link = soup.find("a")

print(link["href"])

Output:

/products


------------------------------------------------------------------------------------------------
22. What happens if the attribute doesn't exist?

This:

element["href"]

can raise a KeyError.

Safer:

element.get("href")


------------------------------------------------------------------------------------------------
23. How do you extract an image URL?

HTML:

<img src="product.jpg">

Python:

img = soup.find("img")

url = img.get("src")

print(url)


------------------------------------------------------------------------------------------------
24. How do you extract multiple links?
links = soup.find_all("a")

for link in links:
    print(
        link.get_text(strip=True),
        link.get("href")
    )
    
    
Part 5 — CSS Selectors


------------------------------------------------------------------------------------------------
25. What is select() in BeautifulSoup?

select() allows CSS selectors.

Example:

elements = soup.select(
    ".product"
)


------------------------------------------------------------------------------------------------
26. How do you select an ID?
soup.select("#product")

Equivalent conceptually to:

#product


------------------------------------------------------------------------------------------------
27. How do you select a class?
soup.select(".product")


------------------------------------------------------------------------------------------------
28. How do you select a tag?
soup.select("h1")


------------------------------------------------------------------------------------------------
29. How do you select nested elements?

HTML:

<div class="product">
    <span class="price">$100</span>
</div>

Python:

price = soup.select_one(
    ".product .price"
)


------------------------------------------------------------------------------------------------
30. Difference between select_one() and select()?
select_one()
    ↓
first matching element

select()
    ↓
all matching elements


Part 6 — Coding Questions

------------------------------------------------------------------------------------------------
31. Coding: Extract all headings
Question

Extract all <h2> text.

Answer
headings = soup.find_all("h2")

for heading in headings:
    print(heading.get_text(strip=True))



------------------------------------------------------------------------------------------------
32. Coding: Extract all links
links = soup.find_all("a")

for link in links:
    text = link.get_text(strip=True)
    href = link.get("href")

    print(text, href)
    
    
    
------------------------------------------------------------------------------------------------
33. Coding: Extract product names and prices

Suppose HTML looks like:

<div class="product">
    <h2 class="name">Laptop</h2>
    <span class="price">$999</span>
</div>

Code:

products = soup.find_all(
    "div",
    class_="product"
)

for product in products:

    name = product.select_one(
        ".name"
    ).get_text(strip=True)

    price = product.select_one(
        ".price"
    ).get_text(strip=True)

    print(name, price)


------------------------------------------------------------------------------------------------
34. Coding: Scrape a table
table = soup.find("table")

rows = table.find_all("tr")

for row in rows:

    cells = row.find_all(
        ["th", "td"]
    )

    data = [
        cell.get_text(strip=True)
        for cell in cells
    ]

    print(data)


------------------------------------------------------------------------------------------------
35. Coding: Extract only links containing a particular URL
links = soup.find_all("a")

for link in links:

    href = link.get("href")

    if href and "/product/" in href:
        print(href)
        
        
        
------------------------------------------------------------------------------------------------
36. Coding: Handle missing elements

Bad:

price = soup.find(
    "span",
    class_="price"
).text

If the element doesn't exist, this can fail.

Better:

element = soup.find(
    "span",
    class_="price"
)

price = (
    element.get_text(strip=True)
    if element
    else None
)

This is an important production-quality practice.



------------------------------------------------------------------------------------------------
37. Coding: Create a reusable scraper
import requests
from bs4 import BeautifulSoup


def get_page(url):

    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    return BeautifulSoup(
        response.text,
        "html.parser"
    )


soup = get_page(
    "https://example.com"
)

print(soup.title.get_text(strip=True))


------------------------------------------------------------------------------------------------
38. Coding: Extract page title
title = soup.title

if title:
    print(title.get_text(strip=True))
39. Coding: Extract meta description
meta = soup.find(
    "meta",
    attrs={"name": "description"}
)

description = (
    meta.get("content")
    if meta
    else None
)

print(description)


------------------------------------------------------------------------------------------------
40. Coding: Convert scraped data into dictionaries
products = []

for product in soup.select(".product"):

    name = product.select_one(
        ".name"
    )

    price = product.select_one(
        ".price"
    )

    products.append({
        "name": name.get_text(strip=True)
        if name else None,

        "price": price.get_text(strip=True)
        if price else None
    })

print(products)




------------------------------------------------------------------------------------------------
Part 7 — SDET Scenario Questions
41. The page source contains the data, but BeautifulSoup can't find it. Why?

Possible reasons:

JavaScript rendering

The initial HTML may not contain the data.

For example:

requests
 ↓
HTML
 ↓
No products

But:

Browser
 ↓
JavaScript executes
 ↓
API request
 ↓
Products appear

BeautifulSoup doesn't execute JavaScript.

Solutions include:

Find the underlying API
Use Selenium
Use Playwright



------------------------------------------------------------------------------------------------
42. BeautifulSoup vs Selenium for dynamic websites?

If the data is already in HTML:

requests + BeautifulSoup

If JavaScript generates the data:

Selenium / Playwright

But before using browser automation, checking whether the page calls a public/authorized API is often more efficient.




------------------------------------------------------------------------------------------------
43. How would you scrape a JavaScript-heavy website?

I would first inspect network requests.

Browser
 ↓
Developer Tools
 ↓
Network
 ↓
XHR / Fetch
 ↓
API response

If the required data comes from an accessible API, I can potentially use:

requests

directly.

Otherwise:

Playwright/Selenium

may be appropriate.




------------------------------------------------------------------------------------------------
44. How do you handle pagination?

Suppose:

?page=1
?page=2
?page=3

You can loop:

for page in range(1, 6):

    url = f"https://example.com/products?page={page}"

    response = requests.get(url)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # extract products
    
    
------------------------------------------------------------------------------------------------
45. How do you avoid duplicate data?

Use a set for unique identifiers:

seen = set()

for product in products:

    product_id = product["id"]

    if product_id not in seen:

        seen.add(product_id)

        save(product)
        
        
        
------------------------------------------------------------------------------------------------
46. What if the website returns HTTP 429?

429 means:

Too Many Requests

You should not simply hammer the site harder.

Use responsible request handling such as:

Rate limiting
Backoff
Retry-After when provided
Caching
Fewer requests

Example concept:

import time

time.sleep(2)

For production systems, exponential backoff is preferable to a fixed sleep.



------------------------------------------------------------------------------------------------
47. What is rate limiting?

Rate limiting controls how frequently requests are sent.

Example:

Request
 ↓
Wait
 ↓
Request
 ↓
Wait

This reduces server load and helps avoid triggering rate limits.



------------------------------------------------------------------------------------------------
48. What is a retry mechanism?

If a request temporarily fails:

Request
 ↓
Failure
 ↓
Retry
 ↓
Failure
 ↓
Retry

You should limit retries and use backoff rather than retrying indefinitely.



------------------------------------------------------------------------------------------------
49. What is robots.txt?

robots.txt provides crawling instructions for automated agents.

Example:

https://example.com/robots.txt

It is useful to inspect, but it is not a substitute for understanding the site's terms, access controls, or applicable rules.




------------------------------------------------------------------------------------------------
50. Is web scraping legal?

There isn't a universal yes/no answer.

It depends on factors such as:

What data is being collected
Whether it is public
Website terms
Copyright/database rights
Privacy laws
Rate/load
Authentication/access restrictions
Your jurisdiction and use case

For interview purposes:

"I scrape only where I have authorization or the use is permitted, respect access controls and site terms, minimize request load, and avoid collecting sensitive personal information unnecessarily."

That's a strong professional answer.



------------------------------------------------------------------------------------------------
Part 8 — Advanced Questions
51. What is the difference between .text and .get_text()?

BeautifulSoup tags expose .text as a convenient way to retrieve descendant text.

get_text() provides more control.

Example:

element.get_text(
    separator=" ",
    strip=True
)

This is useful when HTML contains nested elements and you want clean output.



------------------------------------------------------------------------------------------------
52. What is prettify()?

It formats parsed HTML in an easier-to-read structure.

print(soup.prettify())

Useful for debugging HTML structure.



------------------------------------------------------------------------------------------------
53. What is decompose()?

It removes a tag and destroys it from the parse tree.

Example:

for script in soup.find_all("script"):
    script.decompose()

Useful when cleaning HTML before extracting text.



------------------------------------------------------------------------------------------------
54. How do you remove HTML tags from content?

BeautifulSoup itself can extract text:

text = soup.get_text(
    " ",
    strip=True
)


------------------------------------------------------------------------------------------------
55. How do you extract only external links?

You could check whether a URL is absolute and belongs to a different domain.

For example:

from urllib.parse import urlparse

base_domain = "example.com"

for link in soup.find_all("a"):

    href = link.get("href")

    if not href:
        continue

    parsed = urlparse(href)

    if parsed.netloc and base_domain not in parsed.netloc:
        print(href)

In a real scraper, domain matching should be implemented carefully rather than using simplistic substring checks.



------------------------------------------------------------------------------------------------
56. How would you save scraped data into CSV?
import csv

with open(
    "products.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["name", "price"]
    )

    writer.writeheader()

    writer.writerows(products)
    
    
------------------------------------------------------------------------------------------------
57. How would you save scraped data into JSON?
import json

with open(
    "products.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        products,
        file,
        indent=4
    )
    
    
------------------------------------------------------------------------------------------------
58. How would you test a web scraper using pytest?

This is particularly relevant to your SDET profile.

Example:

def test_product_name():

    soup = get_page(url)

    product = soup.select_one(
        ".product"
    )

    assert product is not None

You can also validate:

HTTP status
Required elements
Expected number of records
Required fields
Data format
Duplicate records
Missing values



------------------------------------------------------------------------------------------------
59. How would you design a production scraper?

A good answer:

scraper/
│
├── scrapers/
│   └── product_scraper.py
│
├── parsers/
│   └── product_parser.py
│
├── utils/
│   ├── http_client.py
│   └── retry.py
│
├── models/
│   └── product.py
│
├── tests/
│
├── config/
│
└── reports/

Separate:

HTTP fetching
     ↓
HTML parsing
     ↓
Data validation
     ↓
Data storage
     ↓
Testing

This makes the scraper easier to maintain.



------------------------------------------------------------------------------------------------
60. Interview scenario: "Your scraper suddenly stops working. What do you do?"

This is a very good SDET-style question.

I would investigate in this order:

1. HTTP status code
        ↓
2. Response HTML
        ↓
3. Page structure changed?
        ↓
4. Locator changed?
        ↓
5. JavaScript rendering changed?
        ↓
6. Authentication/session issue?
        ↓
7. Rate limiting?
        ↓
8. API changed?
        ↓
9. Network/DNS issue?
        ↓
10. Site blocking automated requests?

I would compare the current response against a previously known-good response and add tests around important selectors/data fields so structural changes are detected early.





------------------------------------------------------------------------------------------------
🔥 15 Coding Problems You Should Actually Practice

For your SDET interview, I recommend implementing these yourself rather than just reading the answers:

Easy
Extract all <h1> tags.
Extract all links.
Extract all image URLs.
Extract page title.
Extract elements by class.
Extract elements by ID.


Medium
Scrape product name + price.
Scrape an HTML table.
Handle missing elements.
Handle pagination.
Remove duplicate products.
Save results to CSV.
Save results to JSON.


SDET-level
Build a reusable scraper class.
class WebScraper:

    def get_page(self, url):
        pass

    def parse_products(self, html):
        pass

    def save_results(self, data):
        pass

Build pytest tests for your scraper.
test_status_code()
test_product_exists()
test_product_has_price()
test_no_duplicate_products()
test_required_fields_present()


"""
