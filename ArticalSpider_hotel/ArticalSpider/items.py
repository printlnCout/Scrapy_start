# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,Join,TakeFirst


class ArticalspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def add_jobbole(value):
    return value+"-bobby"

def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except:
        create_date = datetime.datetime.now().date()
    return create_date


def return_value(value):
    return value


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


def remove_comment_tags(value):
    if "评论" in value:
        return ""
    else:
        return value

def move_strip_from(value):
    value.replace("\n","")
    value.replace(" ", "")
    return value

def move_strip_destinction(value):
    value.replace("\n", "")
    value.replace(" ", "")
    return value

class ArticalItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

class HotelItem(scrapy.Item):
    img_url = scrapy.Field()
    # image=scrapy.Field()
    # image_path=scrapy.Field()
    # img_local_url = scrapy.Field()
    big_name = scrapy.Field()
    small_name = scrapy.Field()
    star_count = scrapy.Field()
    user_rating = scrapy.Field()
    location = scrapy.Field()
    comment = scrapy.Field()
    comments_all = scrapy.Field()
    comments_url = scrapy.Field()
    look_for_more = scrapy.Field()
    money_pernight = scrapy.Field()

class QiongYouWangItemUnit_FirstLast(scrapy.Item):
    from_location = scrapy.Field(
        input_processor=MapCompose(move_strip_from),
        output_processsor = Join(",")
    )
    destinction = scrapy.Field(
        input_processor=MapCompose(move_strip_destinction),
        output_processsor = MapCompose(return_value)
    )
    distance = scrapy.Field()
    #Single_day_trip = scrapy.Field()

class QiongYouWangItemUnit_Place(scrapy.Item):
    #feature = scrapy.Field()
    #image = scrapy.Field()
    place_url = scrapy.Field()
    place_name = scrapy.Field()
    Star_counting = scrapy.Field()
    comments_count = scrapy.Field()
    comments = scrapy.Field()
    user_url = scrapy.Field()
    #list = scrapy.Field()
    #ranking = scrapy.Field()


class QiongYouWangItem_Place(scrapy.Item):
    a=scrapy.Field()

class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor = MapCompose(date_convert)
    )
    url=scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processsor=MapCompose(return_value)
    )
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processsor=Join(",")
    )
    content = scrapy.Field()

    #_id = Field()