import scrapy  

class firstSpider(scrapy.Spider): 
    name = "first" 
    # allowed_domains = ["dmoz.org"] 
   
    # start_urls = [ 
    #   "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/", 
    #   "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/" 
    # ]  
    allowed_domains = ["udacity.com"] 
    
    start_urls = [ 
        "https://www.udacity.com/courses/all"
    ]  
    def parse(self, response): 
        filename = response.url.split("/")[-2]
        with open(filename+ '.html', 'wb') as f: 
            f.write(response.body)
        with open(filename+ '.csv', 'w') as f:
            f.writerow([res for res in response.body])