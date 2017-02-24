from scrapy import Spider,Request
from bs4 import BeautifulSoup


class BaiduTopSpider(Spider):
    name = 'baidu_top'
    start_urls='http://top.baidu.com/news/pagination?pageno={}'