import scrapy
from scrapy.crawler import CrawlerProcess

class DCspider(scrapy.Spider):

    name = "dc_spider"

    def start_requests(self):
        urls = ["http://www.datacamp.com/courses/all"]
        for url in urls:
            yield scrapy.Request( url = url, callback = self.parse )

    def parse(self, response):
        
        html_file = "DC_courses.html"
        with open( html_file, "wb") as fout:
            fout.write( response.body )

        csv_file = "DC_courses.csv"
        with open( csv_file, "w" ) as f:
            f.writelines([ link + '/n' for link in links])

        links = response.css('div.course-block > a::attr(href)').extract()
        
        for link in links:
            yield response.follow( url = link, callback = self.parse2)
    
    def parse2(self, response):
        #parse the course site here.
        crs_title = response.xpath('//h1[contains(@class,"titles")]/text()')
        crs_title_txt = crs_title.extract_first().strip()

        ch_titles = response.css( 'h4.chapter__title::text')
        ch_titles.txt = [t.strip() for t in ch_titles.extract()]

        dc_dict[crs_title_txt] = [ch_titles_txt]

        print(dc_dict)

        html_file = "DC_courses.html"
        with open( html_file, "wb") as fout:
            fout.write( response.body )

        csv_file = "DC_courses.csv"
        with open( csv_file, "w" ) as f:
            f.writelines([ link + '/n' for link in links])

dc_dict = dict()

process = CrawlerProcess()

process.crawl(DCspider)

process.start()
