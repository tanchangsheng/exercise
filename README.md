# exercise

##Task Chosen
A. Write a simple Python web crawler to retrieve latest news from a news portal periodically.

##About Task

###1. Installed Scrapy and created a Scrapy project
Decided to use Scrapy, an open source Python library for web scraping because it has the necessary web scraping functions needed for scraping news and being open source there is a lot of support from the online community.

###2. Written a simple web crawler to crawl for the Title and Url of news from http://www.kdnuggets.com/news/index.html
The web crawler crawls for 2017 news. The exact code of the spider can be found at in the project directory ScrapingScraper/spiders/newsSpider.py

###3. Deployed the spider on https://scrapinghub.com/ and set crawler to run every day at 0000 hours.
Scrapinghub allows deployment and scheduling of running spiders. I deployed my project on this site and set a periodic job everday at 0000.

###4. Would be able to retrieve the scraping results in the form of json.
