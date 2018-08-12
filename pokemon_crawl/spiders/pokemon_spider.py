#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 12:04:04 2017

@author: yuying68
"""
import scrapy
from items import PokemonCrawlItem 


class MyPokemon(scrapy.Spider):
    name = "MyPokemon"
    start_urls = [
        'https://pokemondb.net/pokedex/national'
    ]
       


#
#    
    def parse(self, response):
        a = response.css("span.infocard-tall")
        for i in a:
            yield {
                'Number': [i.css('small::text').extract_first()],
                'Name': [i.css("a.ent-name::text").extract_first()],
                }
#            
        link = response.css('span.infocard-tall a.ent-name::attr(href)')
        for j in link:
            yield response.follow(j, callback=self.parse2)
#            
    def parse2(self,response):  
        yield{
            'Number': response.css("table.vitals-table tr td strong::text").extract_first(),
             'Name': response.css("h1::text").extract(), 
            'Pokedex Entry': [response.css("table.vitals-table tbody td::text").re(r'^([A-Z].{3,}[.]$)')[0]]
                }


#meta method

    def parse(self, response):
        #item = PokemonCrawlItem()
        link = response.css('span.infocard-tall a.ent-name::attr(href)').extract()
        b = response.css("span.infocard-tall")
        url_1 = []
        
        
        for i in b:
            item = PokemonCrawlItem()
            item['Name'] = i.css('a.ent-name::text').extract_first()
            item['Number']= i.css('small::text').extract_first()
        
            
            
            url_1 = i.css('a.ent-name::attr(href)').extract()
            url = "https://pokemondb.net" + url_1[0].encode('utf-8')
            
            request = scrapy.Request(url, callback=self.parse2)
            request.meta['Name'] = item
            request.meta['Number'] = item
            
            yield request

        
    def parse2(self, response):
        item = response.meta['Name']
        item = response.meta['Number']

        item['text'] = response.css("table.vitals-table tbody td::text").re(r'^([A-Z].{3,}[.]$)')[0]
        yield item
