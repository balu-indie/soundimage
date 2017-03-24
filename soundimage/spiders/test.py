#from scrapy.spiders.Spider import BaseSpider
import scrapy
#import xpath 
#from scrapy.selector import HtmlXPathSelector
from soundimage.items import SoundimageItem


class BlogSpider(scrapy.Spider):
    name = "sound"
    allowed_domains = ["soundimmage.com"]
    start_urls = ["http://soundimage.org/fantasywonder/"]

    def parse(self, response):
        #hxs = xpath(response)
        titles = response.xpath('//*[contains(@class,"wp-audio-shortcode")]/a/text()').extract()
        for links in titles:
            print(links)
        return links
        
       
