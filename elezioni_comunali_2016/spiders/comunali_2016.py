# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.request import Request

from elezioni_comunali_2016.items import Candidato, Lista

import string

idComune = 0

sindaco = True

class Comunali2016Spider(CrawlSpider):
    name = 'comunali-2016'
    allowed_domains = ['elezioni.interno.it']
    start_urls = ['http://elezioni.interno.it/comunali/scrutini/20160605/G000.htm']

    download_delay=0.5

    custom_settings = {
        'MODE': 'sindaco',
    }

    def parse(self, response):

        global sindaco
        mode = self.settings.get('MODE')

        if mode == 'lista':
           sindaco = False

        print sindaco

        counter = 0
        for line in response.xpath('//table[@class="tblMonitor"]/tr/td[1]/a'):
            counter+=1
            href = line.xpath('@href')
            url = response.urljoin(href.extract()[0])
            yield Request(url, callback=self.parse_province)
 

    def parse_province(self, response):
        counter = 0
        for line in response.xpath('//table[@class="tblMonitor"]/tr/td[1]/a'):
            counter+=1
            href = line.xpath('@href')
            url = response.urljoin(href.extract()[0])
            yield Request(url, callback=self.parse_comune)


    def parse_comune(self, response):
        global idComune
        global sindaco

        regione = response.xpath('//ul[@class="breadcrumb"]/li[4]/a/text()').extract()[0][5:]
        provincia = response.xpath('//ul[@class="breadcrumb"]/li[5]/a/text()').extract()[0][6:]
        comune = response.xpath('//ul[@class="breadcrumb"]/li[6]/text()').extract()[0]

        idComune += 1
        candidato = ''
        voti = ''

        if response.xpath('//table[@class="tblScrutini"]/tr[@class="dott"]').extract_first() is not None:
          for line in response.xpath('//table[@class="tblScrutini"]/tr'):
              value = line.xpath('self::*[@class="evid"]')
              list = line.xpath('self::*[@class="dott"]')
              if value.extract_first() is not None:
                 candidato = value.xpath('./th/div/text()').extract()[0]
                 if sindaco:
                    i = Candidato()
                    i['nome'] = candidato
                    i['voti'] = string.replace(value.xpath('./td[3]/text()').extract()[0], '.', '')
                    i['regione'] = regione
                    i['provincia'] = provincia
                    i['comune'] = comune
                    i['anno'] = '2016'
                    yield i
              elif (list.extract_first() is not None) and not sindaco:
                 l = Lista()
                 l['idCandidato'] = candidato
                 l['nome'] = list.xpath('./td[3]/text()').extract()[0]
                 l['voti'] = string.replace(list.xpath('./td[7]/text()').extract()[0], '.', '')
                 l['regione'] = regione
                 l['provincia'] = provincia
                 l['comune'] = comune
                 l['anno'] = '2016'
                 yield l
              else:
                pass
        else:
          for line in response.xpath('//table[@class="tblScrutini"]/tr'):
              value = line.xpath('self::*[@class="evid"]')
              list = line.xpath('self::*/td/img/@alt')
              if value.extract_first() is not None:
                 candidato = value.xpath('./th/div/text()').extract()[0]
                 voti = string.replace(value.xpath('./td[3]/text()').extract()[0], '.', '')
                 if sindaco:
                    i = Candidato()
                    i['nome'] = candidato
                    i['voti'] = voti
                    i['regione'] = regione
                    i['provincia'] = provincia
                    i['comune'] = comune
                    i['anno'] = '2016'
                    yield i
              elif (list.extract_first() is not None) and not sindaco:
                 l = Lista()
                 l['idCandidato'] = candidato
                 l['nome'] = list.extract()[0]
                 l['voti'] = voti
                 l['regione'] = regione
                 l['provincia'] = provincia
                 l['comune'] = comune
                 l['anno'] = '2016'
                 yield l
              else:
                 pass
#        if not sindaco:
#           for line in response.xpath('//table[@class="tblRiepScrutini"][2]//tr'):
#              l = Lista()
#              l['idCandidato'] = line.xpath('./th/text()').extract()[0]
#              l['nome'] = line.xpath('./th/text()').extract()[0]
#              l['voti'] = string.replace(line.xpath('./td[@class="num"]/text()').extract()[0], '.', '')
#              l['regione'] = regione
#              l['provincia'] = provincia
#              l['comune'] = comune
#              l['anno'] = '2016'
#              yield l

