import scrapy
# from tutorial.items import DmozItem

class MyprojectSpider(scrapy.Spider):
    name = "project"
    allowed_domains = ["udacity.com"]
    
    start_urls = [
        "http://www.udacity.com/courses/all"
    ]
    def parse(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback = self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print (title, link, desc)
            
            # item = DmozItem()
            # item['title'] = sel.xpath('a/text()').extract()
            # item['link'] = sel.xpath('a/@href').extract()
            # item['desc'] = sel.xpath('text()').extract()
            # print(item)
            # yield item

    # def parse_articles_follow_next_page(self, response):
    #     for article in response.xpath("//article"):
    #     item = ArticleItem()
        
    #     ... extract article data here

    #     yield item

    #     next_page = response.css("ul.navigation > li.next-page > a::attr('href')")
    #     if next_page:
    #         url = response.urljoin(next_page[0].extract())
    #         yield scrapy.Request(url, self.parse_articles_follow_next_page)