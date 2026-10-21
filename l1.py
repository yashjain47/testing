"""
:::::::::::::::::::::::::::::::: Web Scraping ::::::::::::::::::::::::::::::::

Automatic method to get/obtain large amount of data from the websites.
It extracts underlying HTML code and with it, data storeed in the database.  The scraper can then replicateswebsites content elsewhere. 


Web crawler
crawler >> visits all links >> build list >> indexing >> database


Web scraper
website >> scraper  >> XML
                    >> SQL
                    >> Json, etc
                    
                    
                    
Types of scraper:

1.  self-built web scraper
2.  Pre-built web scraper
3.  Browser extension web scraper
4.  Software web scraper
5.  Cloud web scraper


Tools:

1.  scrapy
2.  BeautifulSoap
3.  Selenium


Legality of web scraping:

1.  consiider /robot.txt file for scraping any website.
2.  Give priority to API if provided.
3.  scrape the website with slow rate of request to fetch the data.
4.  Follow rules and standard of the website.





Kinds of Objects

1.  Tag
2.  NavigableString
3.  BeautifulSoap
4.  Comments





"""

# import requests
# from bs4 import BeautifulSoup


# response = requests.get("https://www.tutorialsfreak.com")
# print(response.status_code)
# print(response.url,"\n")
# content = response.content

# soap = BeautifulSoup(content,"html.parser")
# print(soap.prettify())

# print(soap.title)
# print(soap.title.name)
# print(soap.title.text)

# print(soap.p)
# print(soap.p.name)
# print(soap.p.text)


# print(soap.find_all('p'))





# import requests
# from bs4 import BeautifulSoup

# url = "https://webscraper.io/test-sites/e-commerce/allinone"

# response = requests.get(url)
# print(response.status_code)
# content = response.content
# # print(response.text)

# soap = BeautifulSoup(content, "html.parser")
# # print(soap)

# boxes = soap.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")












