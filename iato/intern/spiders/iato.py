# -*- coding: utf-8 -*-
import scrapy
from intern.items import InternItem 
from scrapy.selector import Selector 

class IatoSpider(scrapy.Spider):
    name = 'iato'
    allowed_domains = []
    start_urls = ['http://www.iato.in/members/lists/']
    def parse(self, response):
        #extracting links
        hrefs = response.xpath('//tr/td/a/@href').extract()
        for href in hrefs:   #looping through the links
        	url=response.urljoin(href)
        	yield scrapy.Request(url=url, callback=self.parse_attr)  #scraping the links one by one 

    #function for link scraping
    def parse_attr(self,response):
    	para = [''.join(td.xpath('./text()').extract()) for td in Selector(response).xpath('//div[contains(h6,"Contact")]/p')]
    	#spaces for avoiding null values and getting div containing contact Info 
    	item=InternItem()  #item class defined at items.py

    	#getting all items and saving it into different columns
    	item['company_name']=para[0]
    	item['contact_person']=para[1]
    	item['designation']=para[2]
    	item['street_Address']=para[3]
    	item['city']=para[4]
    	item['state']=para[5]
    	item['pincode']=para[6]
    	item['email']=para[7]
    	item['phone']=para[8]
    	item['mobile']=para[9]
    	item['fax']=para[10]
    	item['website']=para[11]
    	yield item
    	
        
        
        