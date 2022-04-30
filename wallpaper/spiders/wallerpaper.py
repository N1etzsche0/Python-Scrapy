import scrapy

from ..items import WallpaperItem


class WallerpaperSpider(scrapy.Spider):
    name = 'wallerpaper'
    allowed_domains = ['wallpapershome.com']
    start_urls = ['https://wallpapershome.com/?page=' + str(x) for x in range(1, 2)]


    def parse(self, response):
        src_list = response.xpath('//div[@id="pics-list"]/p/a/@href').extract()
        for src in src_list:
            yield scrapy.Request(url='https://wallpapershome.com' + str(src), callback=self.get_info)

    def get_info(self, response):
        src_list = response.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div/div/div[2]/p[1]/a/@href').extract()
        for src in src_list:
            item = WallpaperItem()
            src = 'https://wallpapershome.com' + str(src)
            item['src'] = [src]
            print(item)
            yield item
