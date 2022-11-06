from pickle import FALSE, TRUE
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapysexkeyword.commandline import get_command_line
import random
import string
from .scrapysexkeyword.spiders.keyword_spider import KeywordSpider
import hashlib
import os
import logging
import validators
from .config import get_config

logger = logging.getLogger(__name__)


class WrongConfigurationError(Exception):
    pass

def main(return_results=False, parse_cmd_line=True, config_from_dict=None,external_config_file_path=None):
    if parse_cmd_line:
        cmd_line_args = get_command_line()
        if cmd_line_args.get('config_file', None):
            external_config_file_path = os.path.abspath(
                cmd_line_args.get('config_file'))
            logger.info("external config file is {}".format(
                external_config_file_path))

    config = get_config(
        cmd_line_args, external_config_file_path, config_from_dict)
   
    outfile = config.get('output_filename')

    if(outfile is None or len(outfile) < 1):
        outfilename = hashlib.md5(''.join(random.choices(
                string.ascii_lowercase, k=32)).encode('utf-8')).hexdigest()

        outfile = './output/'+outfilename+".json"

    SETTINGS = {
            "FEEDS": {
                outfile: {"format": "json"},
            },
            # "DOWNLOADER_MIDDLEWARES": {
            #     'emailscrapy.emailscrapy.middlewares.CustomProxyMiddleware': 350,
            #     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
            #     'emailscrapy.emailscrapy.middlewares.EmailscrapyDownloaderMiddleware': 543,
            # },
            "HTTPCACHE_ENABLED":False,
            "ROBOTSTXT_OBEY": config.get('ROBOTSTXT_OBEY',True),
            # "SELENIUM_DRIVER_NAME": config.get("SELENIUM_DRIVER_NAME","chrome"),
            # "SELENIUM_DRIVER_EXECUTABLE_PATH":config.get("SELENIUM_DRIVER_EXECUTABLE_PATH"),
            # "SELENIUM_DRIVER_ARGUMENTS":config.get("SELENIUM_DRIVER_ARGUMENTS"),
            # "SELENIUM_DRIVER_ARGUMENTS":config.get("SELENIUM_DRIVER_ARGUMENTS"),
            # "DOWNLOADER_MIDDLEWARES": {
            #     'scrapy_selenium.SeleniumMiddleware': 800
            # }
        }
    useProxy=config.get('proxy',False)

    if useProxy==True:
       logger.info("use proxy") 
       SETTINGS['DOWNLOADER_MIDDLEWARES']={
                'scrapysexkeyword.middlewares.CustomProxyMiddleware': 350,
                'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
                'scrapysexkeyword.middlewares.EmailscrapyDownloaderMiddleware': 543,
       }
    process = CrawlerProcess(SETTINGS)
    process.crawl(KeywordSpider, output=outfile)
    process.start()
