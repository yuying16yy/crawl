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
#    def parse(self, response):
##        a = response.css("span.infocard-tall")
##        for i in a:
##            yield {
##                'Number': [i.css('small::text').extract_first()],
##                'Name': [i.css("a.ent-name::text").extract_first()],
##                }
#            
#        link = response.css('span.infocard-tall a.ent-name::attr(href)')
#        for j in link:
#            yield response.follow(j, callback=self.parse2)
#            
#    def parse2(self,response):  
#        yield{
#            'Number': response.css("table.vitals-table tr td strong::text").extract_first(),
#             'Name': response.css("h1::text").extract(), 
#            'Pokedex Entry': [response.css("table.vitals-table tbody td::text").re(r'^([A-Z].{3,}[.]$)')[0]]
#                }
        
    def parse(self, response):
        link = response.css('span.infocard-tall a.ent-name::attr(href)')
        a = response.css("span.infocard-tall")
        item = PokemonCrawItem()
        for i in a:
            item['Number']= [i.css('small::text').extract_first()]
            item['Name']=[i.css("a.ent-name::text").extract_first()]
            link = [i.css('a.ent-name::attr(href)')]
                
        
            yield scrapy.Request(link,meta = {'key':item}, callback=self.parse2)
        
        
        
        
        
    def parse2(self, response):
        item = response.meta['key']
        item['text'] = [response.css("table.vitals-table tbody td::text").re(r'^([A-Z].{3,}[.]$)')[0]]
        yield item

#    def parse_page2(self, response):
#        item = response.meta['item']
#        item['other_url'] = response.url
#        yield item







           
#    def parse_page1(self):
#        yield scrapy.Request('https://pokemondb.net/pokedex/%s' % self.Name)
#            


#
#a = response.css("span.infocard-tall small::text").extract()       
#b = response.css("a.ent-name::text").extract()
#b=[]
#for i in a:
#    b += [i.css("small::text").extract_first()]
#link = response.css('span.infocard-tall  a.ent-name::attr(href)')
#poke = response.css("table.vitals-table tbody td::text").re(r'^([A-Za-z].+$)')
        
        
        
        
        
#import scrapy
#
#class MyPokemon(scrapy.Spider):
#    name = "MyPokemon"
#    start_urls = [
#        'https://pokemondb.net/pokedex/national'
#    ]
#
#    
#    def parse(self, response):
##        a = response.css("span.infocard-tall")
##        for i in a:
##            yield {
##                'Number': [i.css('small::text').extract_first()],
##                'Name': [i.css("a.ent-name::text").extract_first()],
##                }
#            
#        link = response.css('span.infocard-tall  a.ent-name::attr(href)')
#        for j in link:
#            yield response.follow(j, callback=self.parse2)
#            
#    def parse2(self,response):  
#        yield{
#            'Pokedex Entry': [response.css("table.vitals-table tbody td::text").re(r'^([A-Z].{3,}[.]$)')[0]]
#                }
#        
#            