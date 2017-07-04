# -*- coding: utf-8 -*-
import os
# Scrapy settings for ArticalSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ArticalSpider'

SPIDER_MODULES = ['ArticalSpider.spiders']
NEWSPIDER_MODULE = 'ArticalSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ArticalSpider (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

ROBOTSTXT_OBEY = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED=False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ArticalSpider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ArticalSpider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'ArticalSpider.pipelines.QunarspiderPipeline': 300,
    #'ArticalSpider.pipelines.ArticleImagePipeline': 200
}
MONGODB_SERVER="127.0.0.1"
MONGODB_PORT=27017
MONGODB_DB="QiongYou"
MONGO_DB_COLLECTTION="ALL_COUNTRY"
# IMAGE_STORE="/home/lei/data/Image"
# IMAGES_RESULT_FIELD = '/home/lei/data/Image'
IMAGES_URLS_FIELD ="image_url"  #image_url是在items.py中配置的网络爬取得图片地址

project_dir=os.path.abspath(os.path.dirname(__file__))  #获取当前爬虫项目的绝对路径
IMAGES_STORE=os.path.join(project_dir,'images')  #组装新的图片路径


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
AUTOTHROTTLE_ENABLED=True
# The initial download delay
AUTOTHROTTLE_START_DELAY=5
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED=True
HTTPCACHE_EXPIRATION_SECS=0
HTTPCACHE_DIR='httpcache'
HTTPCACHE_IGNORE_HTTP_CODES=[]
HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
