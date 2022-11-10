import scrapy
import logging
from scrapysexkeyword.scrapysexkeyword.items import ScrapysexkeywordItem
# from scrapysexkeyword.scrapysexkeyword.iso3166 import ISO3166

logger = logging.getLogger(__name__)
class KeywordSpider(scrapy.Spider):
    name = "keyword"

    def __init__(self, output='', **kwargs):
        self.output=output
        super().__init__(**kwargs)
    def start_requests(self):
        meta = {'REDIRECT_ENABLED':True}
        # urls = []
        # for x in ISO3166:
        #     urls.append('https://www.xvideos.com/change-country/'+x.lower())     
        # logger.info(urls)
        urls = [
            # 'https://www.xvideos.com/change-country/au',
            'https://www.xvideos.com/change-country/us',
            # 'https://www.xvideos.com/change-country/at',       
        ]
        for url in urls:
            productResponse=scrapy.Request(url=url, callback=self.parse,meta=meta)
            # productResponse.meta['dont_cache'] = True
            yield productResponse

    def parse(self, response):
        for li in response.xpath('//*[@id="main-cat-sub-list"]//li'):
            Item=ScrapysexkeywordItem()
            # logger.info(li)
            keywd=li.xpath('a/text()').extract()
            if(len(keywd)>0):
                Item['keyword']=keywd[0]
            
            yield Item