# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Candidato(scrapy.Item):
    nome = scrapy.Field()
    regione = scrapy.Field()
    provincia = scrapy.Field()
    comune = scrapy.Field()
    voti = scrapy.Field()
    anno = scrapy.Field()

class Lista(scrapy.Item):
    idCandidato = scrapy.Field()
    nome = scrapy.Field()
    regione = scrapy.Field()
    provincia = scrapy.Field()
    comune = scrapy.Field()
    voti = scrapy.Field()
    anno = scrapy.Field()
