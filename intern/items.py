# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InternItem(scrapy.Item):
    # define the fields for your item here like:
     company_name = scrapy.Field()
     contact_person=scrapy.Field()
     designation=scrapy.Field()
     street_Address=scrapy.Field()
     city=scrapy.Field()
     state=scrapy.Field()
     pincode=scrapy.Field()
     email=scrapy.Field()
     phone=scrapy.Field()
     mobile=scrapy.Field()
     fax=scrapy.Field()
     website=scrapy.Field()
     
    
