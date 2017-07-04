# -*- coding: utf-8 -*-
import scrapy
import urllib
import os
from scrapy.http import Request
from urllib import parse
from ArticalSpider.common import get_md5
from ArticalSpider.items import HotelItem,ArticalItemLoader

class JobboleSpider(scrapy.Spider):
    name = "qiongyou"
    imagePath="/home/lei/Image"
    href_base="http://hotel.qyer.com"
    allowed_domains = ["hotel.qyer.com"]
    start_urls = ['http://hotel.qyer.com/']

    def parse(self, response):
        """
        1. 获取文章列表页中的文章url并交给scrapy下载后并进行解析
        2. 获取下一页的url并交给scrapy进行下载， 下载完成后交给parse
        """

        post_node_countrys=response.css("div.pl_footerSeo section.pl_footerSeo__box ul.clearfix li a::attr(href)").extract()
        for post_node_country in post_node_countrys:
            yield Request(url=post_node_country, callback=self.parse_country)

    def parse_country(self,response):
        #解析列表页中的所有文章url并交给scrapy下载后并进行解析
        post_nodes= response.css("ul.cityList.clearfix li")
        for post_node in post_nodes:
            city_url=post_node.css("a::attr(href)").extract_first("")
            yield Request(url=city_url, callback=self.parse_more)

        #提取下一页并交给scrapy进行下载


    def  parse_more(self, response):
        city_name=response.css("div.hotellist_title h1::text").extract_first("").strip()

        next_url = response.css("a.ui_page_next::attr(href)").extract_first("")
        if next_url:
            yield scrapy.FormRequest(url=parse.urljoin(self.href_base, next_url), callback=self.parse_detail)

    def parse_detail(self, response):

        hotel_nodes=response.css("ul.hl_mainlist li")
        for hotel_node in hotel_nodes:

            item_loader = HotelItem()

            big_name = hotel_node.css("p.h_cntitle a::text").extract_first("")
            item_loader["big_name"]=big_name

            small_name = hotel_node.css("p.h_entitle a::text").extract_first("")
            item_loader["small_name"] = small_name

            #下载图片到本地
            img_url = hotel_node.css("div.hl_mainlist__lf a img::attr(data-original)").extract_first("")
            item_loader["img_url"] = img_url
            # res = urllib.request.urlopen(img_url)
            # filename = os.path.join(self.imagePath, big_name + '.jpg')
            # with open(filename, 'wb')as f:
            #     f.write(res.read())
            #
            # item_loader["img_local_url"] = filename

            star_count = len(hotel_node.css("p.h_cntitle i.iconfont.star").extract())
            item_loader["star_count"] = star_count

            user_rating =hotel_node.css("a.grade::text").extract_first("")
            user_rating=user_rating.replace("用户评分","")
            item_loader["user_rating"] = user_rating

            location = hotel_node.css("p.h_level a[title]::text").extract()
            item_loader["location"] = location

            comment = hotel_node.css("p.h_desc a::text").extract_first("")
            comment.replace("\r","")
            item_loader["comment"] = comment

            comments_all = hotel_node.css("p.h_comment a::text").extract_first("")
            user=hotel_node.css("p.h_comment i::text").extract_first("")
            comments_all=comments_all+user
            item_loader["comments_all"] = comments_all

            look_for_more = hotel_node.css("p.h_desc a::attr(href)").extract_first("")
            look_for_more=self.href_base+look_for_more
            item_loader["look_for_more"] = look_for_more

            yield item_loader
